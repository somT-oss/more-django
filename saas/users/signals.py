from django.db.models.signals import post_save # type: ignore
from django.dispatch import receiver

from .models import CustomUser, BusinessOwnerProfile, BuyerProfile

@receiver(post_save, sender=CustomUser)
def create_business_profile(instance, created, **kwargs):
    if created:
        is_seller = instance.is_seller
        first_name = instance.first_name
        last_name = instance.last_name
        business_name = f"{first_name} {last_name}"
        if is_seller:
            business_owner_profile = BusinessOwnerProfile.objects.create(user=instance, business_name=business_name)
            business_owner_profile.save()

@receiver(post_save, sender=CustomUser)
def create_buyer_profile(instance, created, **kwargs):
    if created:
        is_buyer = instance.is_buyer
        if is_buyer:
            buyer_profile = BuyerProfile.objects.create(user=instance)
            buyer_profile.save()
