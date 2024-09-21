from django.contrib import admin
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmini(admin.ModelAdmin):
    """
    Custom custom user admin handler
    """
    list_display = ("first_name", "last_name", "is_seller")
