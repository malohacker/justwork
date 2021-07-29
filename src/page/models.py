from django.db import models


class BaseTitle(models.Model):
    class Meta:
        abstract = True

    title = models.CharField('Title', max_length=100)

    def __str__(self):
        return self.title


class MediaContentType(BaseTitle):
    name = models.CharField('Тип контента', max_length=30)
    schema = models.JSONField(default=dict)


class Content(BaseTitle):
    counter = models.IntegerField('Counter', default=0)
    media_content_type = models.ForeignKey(MediaContentType, on_delete=models.CASCADE)
    spec_attrs = models.JSONField(blank=True, null=True)
    
    def save(self, *args, **kwargs):
        if not self.spec_attrs:
            self.spec_attrs = self.media_content_type.schema
        super(Content, self).save(*args, **kwargs)


class Page(BaseTitle):
    class Meta:
        verbose_name = verbose_name_plural = 'page'

    contents = models.ManyToManyField(Content)



