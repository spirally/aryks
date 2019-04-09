from django.contrib import admin
from .models import Category, Product


# Модель категории
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'alias']
    prepopulated_fields = {'alias': ('name', )}


# Модель товара
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'alias', 'price', 'stock', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'alias': ('name', )}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
