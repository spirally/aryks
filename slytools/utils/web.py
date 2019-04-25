from django.db import models
from django.utils.translation import ugettext_lazy as _


class WebPageMixin(models.Model):

    alias = models.SlugField(max_length=300, db_index=True)
    published = models.BooleanField(default=False, db_index=True, verbose_name=_('Опубликовано'))
    seo_keywords = models.CharField(max_length=512, null=True, blank=True, verbose_name=_('SEO ключевые слова'))
    seo_description = models.TextField(null=True, blank=True, verbose_name=_('SEO описание'))
    content = models.TextField(null=True, blank=True, verbose_name=_('Контент'))
    created = models.DateTimeField(auto_now_add=True, verbose_name=_('Создано'))
    updated = models.DateTimeField(auto_now=True, verbose_name=_('Обновлено'))

    class Meta:
        abstract = True
