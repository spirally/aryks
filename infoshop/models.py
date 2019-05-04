from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.urls import reverse

from slytools.utils.web import WebPageMixin
from slytools.utils.db import IsDeletedModel


# class OwnerType(dict):
#     AUTHOR = 1
#     SCHOOL = 2
#
# OWNER_TYPES = OwnerType({
#     OwnerType.AUTHOR: _(u"Автор"),
#     OwnerType.SCHOOL: _(u"Школа"),
# })


class Owner(IsDeletedModel):
    """
    Владелец продукта
    """
    name = models.CharField(max_length=250, db_index=True, verbose_name=_("Имя"))
    description = models.TextField(blank=True, verbose_name=_('Описание'))
    # type = models.PositiveSmallIntegerField(choices=OWNER_TYPES.items(), verbose_name=_("Тип"))


class School(WebPageMixin, Owner):
    pass


class Author(WebPageMixin, Owner):
    parent = models.ForeignKey(School, on_delete=models.CASCADE, null=True, blank=True, verbose_name=_('Школа'))


class ProductCategory(WebPageMixin, IsDeletedModel):
    """
    Категория каталога
    """
    name = models.CharField(max_length=200, db_index=True, verbose_name=_('Имя'))
    parent = models.ForeignKey("ProductCategory", on_delete=models.CASCADE, null=True, blank=True)

    @property
    def children(self):
        return ProductCategory.objects.filter(parent=self)

    class Meta:
        ordering = ['name']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('infoshop:ProductListByCategory', args=[self.alias])


class Product(WebPageMixin, IsDeletedModel):
    """
    Инфопродукт
    """
    #TODO ManyToMany category
    category = models.ForeignKey(ProductCategory, related_name='products', verbose_name=_("Категория"), on_delete=models.CASCADE)
    owner = models.ForeignKey(Owner, null=True, on_delete=models.CASCADE, verbose_name=_('Автор'))
    name = models.CharField(max_length=250, db_index=True, verbose_name=_("Название"))
    image = models.ImageField(upload_to='products/%Y/%m/%d/', blank=True, verbose_name=_("Изображение"))
    introtext = models.TextField(blank=True, verbose_name=_("Вводный текст"))
    description = models.TextField(blank=True, verbose_name=_("Описание"))
    price = models.DecimalField(null=True, blank=True, max_digits=10, decimal_places=2, verbose_name=_("Цена"))
    price_new = models.DecimalField(null=True, blank=True, max_digits=10, decimal_places=2, verbose_name=_("Новая цена"))
    type_video = models.BooleanField(default=False, verbose_name=_('Смотреть'))
    type_audio = models.BooleanField(default=False, verbose_name=_('Слушать'))
    type_book = models.BooleanField(default=False, verbose_name=_('Читать'))
    type_flow = models.BooleanField(default=False, verbose_name=_('Участвовать'))

    class Meta:
        ordering = ['name']
        index_together = [
            ['id', 'alias']
        ]
        unique_together = [
            ('category', 'alias'),
        ]
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('infoshop:ProductDetail', args=[self.id, self.alias])
