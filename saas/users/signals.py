from django.contrib.auth import get_user_model
from django.db.signals import post_save
from django.dispatch import receiver

from .models import CustomUser, BusinessProfile
