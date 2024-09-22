import uuid
from django.db import models
from django_resized import ResizedImageField
from django.conf import settings


class Products(models.Model):
    """
    Products model class
    """
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=50,
                            null=False,
                            blank=False,
                            help_text="Product name")
    description = models.TextField(max_length=250,
                                   null=False,
                                   blank=False,
                                   help_text="Product description")
    quantity = models.IntegerField(null=False,
                                   blank=False,
                                   default=1,
                                   help_text="Quantity of products available")
    price = models.CharField(
        null=False,
        blank=False,
        help_text="Price of product"
    )
    # TODO: Add product image field after handling static & media files
    # image = models.ResizedImageField(size=[400, 400])

    class Meta:
        verbose_name = 'PRODUCT'
        verbose_name_plural = 'PRODUCTS'

    def __str__(self) -> str:
        return f"{self.name}"
