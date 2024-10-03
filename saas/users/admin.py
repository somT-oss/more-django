from django.contrib import admin
from .models import CustomUser, Community


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    """
    Custom custom user admin handler
    """
    list_display = ("first_name", "last_name", "email", "is_seller")


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
