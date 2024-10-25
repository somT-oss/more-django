from django.contrib import admin
from .models import CustomUser, BusinessOwnerProfile, BuyerProfile

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    """
    Custom user admin handler
    """
    list_display = ("first_name", "last_name", "email", "is_seller")

@admin.register(BusinessOwnerProfile)
class BusinessOwnerProfileAdmin(admin.ModelAdmin):
    """
    Custom business owner profile admin handler
    """
    list_display = "get_buyer_first_name", "get_buyer_last_name"

    def get_buyer_first_name(self, obj) -> str:
        return obj.user.first_name

    def get_buyer_last_name(self, obj) -> str:
        return obj.user.last_name


@admin.register(BuyerProfile)
class BuyerProfileAdmin(admin.ModelAdmin):
    """
    Custom buyer_profile admin handler 
    """
    list_display = "get_buyer_first_name", "get_buyer_last_name"

    def get_buyer_first_name(self, obj) -> str:
        return obj.user.first_name

    def get_buyer_last_name(self, obj) -> str:
        return obj.user.last_name

    get_buyer_first_name.short_description = "first_name" 
    get_buyer_last_name.short_description = "last_name" 



