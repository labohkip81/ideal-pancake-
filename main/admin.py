from django.contrib import admin
from django.utils.html import format_html

from . import models

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'in_stock', 'price')
    list_filter = ('active', 'in_stock', 'date_updated', 'price')
    list_editable = ('in_stock',)
    search_fields = ('name',)
    prepopulated_fields = {"slug":("name",)}
    #readonly_fields = ('slug',)

admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.ProductTag)
admin.site.register(models.ProductImage)