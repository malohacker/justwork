from rest_framework import serializers

from page.models import Page, Content, MediaContentType


class MediaContentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaContentType
        fields = ['title',]


class ContentSerializer(serializers.ModelSerializer):
    media_content_type = MediaContentTypeSerializer(read_only=True)
    class Meta:
        model = Content
        fields = '__all__'


class PageListSerializer(serializers.HyperlinkedModelSerializer):
    # contents = ContentSerializer(read_only=True, many=True)

    class Meta:
        model = Page
        fields = ['url', 'title']


class PageDetailSerializer(serializers.ModelSerializer):
    contents = ContentSerializer(read_only=True, many=True)

    class Meta:
        model = Page
        fields = '__all__'
