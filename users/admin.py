from django.contrib import admin
from .models import User, Address

@admin.register(User)
class AdminUser(admin.ModelAdmin):
    list_display = ["phone", "role", "is_phone_verified", "first_name", "last_name", "email", "username"]
    list_display_links = ["username"]
    readonly_fields = ["is_staff", "is_active", "date_joined"]
    search_fields = ["phone", "email", "first_name", "last_name", "username"]
    list_filter = ["role", "is_phone_verified"]


@admin.register(Address)
class AdminAddress(admin.ModelAdmin):
    list_display = ["user", "province", "city", "address", "postal_code"]
    list_display_links = ["user"]
    search_fields = ["province", "chty", "postal_code"]
    list_filter = ["province"]
    raw_id_fields = ["user"]

    
