from django.contrib import admin
from django.contrib.admin import site
from django_admin_json_editor import JSONEditorWidget

from page.models import Page, MediaContentType, Content


class ContentsInline(admin.StackedInline):
    model = Page.contents.through
    extra = 1


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    fields = ('title', )
    search_fields = ('title', 'contents__title')
    inlines = [
        ContentsInline,
    ]


@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    fields = ('title', 'media_content_type', 'spec_attrs')

    def get_form(self, request, obj=None, **kwargs):
        widget = JSONEditorWidget(getattr(obj, 'spec_attrs', {}), False)
        form = super().get_form(request, obj, widgets={'spec_attrs': widget}, **kwargs)
        return form


@admin.register(MediaContentType)
class MediaContentTypeAdmin(admin.ModelAdmin):
    fields = ('title', 'schema')

    def get_form(self, request, obj=None, **kwargs):
        widget = JSONEditorWidget({}, False)
        form = super().get_form(request, obj, widgets={'schema': widget}, **kwargs)
        return form
