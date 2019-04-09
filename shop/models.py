from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.urls import reverse


# Модель категории
class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True, verbose_name=_('Имя'))
    alias = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:ProductListByCategory', args=[self.alias])


# Модель продукта
class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', verbose_name=_("Категория"), on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True, verbose_name=_("Название"))
    alias = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d/', blank=True, verbose_name=_("Изображение товара"))
    description = models.TextField(blank=True, verbose_name=_("Описание"))
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Цена"))
    stock = models.PositiveIntegerField(verbose_name=_("На складе"))
    available = models.BooleanField(default=True, verbose_name=_("Доступен"))
    created = models.DateTimeField(auto_now_add=True, verbose_name=_('Создан'))
    updated = models.DateTimeField(auto_now=True, verbose_name=_('Обновлен'))

    class Meta:
        ordering = ['name']
        index_together = [
            ['id', 'alias']
        ]
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:ProductDetail', args=[self.id, self.alias])
