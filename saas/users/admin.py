from django.contrib import admin
from .models import CustomUser, Community, BusinessOwnerProfile, BuyerProfile

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



@admin.register(Community)
class CommunityAdmin(admin.ModelAdmin):
    """
    Custom community admin UI handler
    """
    list_display = ("name", "get_community_admin", "get_number_of_community_members")

    def get_community_admin(self, obj) -> str:
        """
        Returns the community admin
        """
        first_name: str = obj.community_owner.first_name
        last_name: str = obj.community_owner.last_name

        return f"{(first_name + last_name).upper()}"

    def get_number_of_community_members(self, obj) -> int:
        """
        Returns the number of community members
        """
        number_of_members: int = obj.community_members.count()

        return number_of_members

    get_community_admin.short_description = "community admin"
    get_number_of_community_members.short_description = "number of community members"
