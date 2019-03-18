from django.contrib import admin
from .models import Product, ProductImages, AttributeProductValue
# Register your models here.

class ProductImagesTabular(admin.TabularInline):
    model = ProductImages
    extra = 0
    min_num = 1

class AttributeProductValueTabular(admin.TabularInline):
    model = AttributeProductValue
    extra  = 0
    min_num = 1

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImagesTabular, AttributeProductValueTabular]

    class Meta:
        model = Product    

admin.site.register(Product, ProductAdmin)
