from django.contrib import admin
from .models import *

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        "title",
    ]

    prepopulated_fields = {
        "slug": ["title"],
    }

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        "name", "price", "stock", "discount_price", "description", "is_active", "created_at"
        ]
    
    prepopulated_fields = {
        "slug": ["name"],
    }
admin.site.register(ProductImage)
