from django.contrib import admin
from .models import ProductCategory, Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'alias']
    prepopulated_fields = {'alias': ('name', )}


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'alias', 'price', 'price_new', 'created', 'updated',]
    list_filter = ['created', 'updated',]
    list_editable = ['price', 'price_new',]
    prepopulated_fields = {'alias': ('name', )}

admin.site.register(ProductCategory, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
