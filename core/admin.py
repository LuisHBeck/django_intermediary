from django.contrib import admin

from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'stock', 'slug', 'creation', 'active']
    list_editable = ['name']
    list_display_links = ['id']
    
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
