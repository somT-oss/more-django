import uuid
import random
from django.db import models
from django.conf import settings
from products.models import Products


class Orders(models.Model):
    """
    Orders model attributes definition
    """
    class OrderStatus(models.TextChoices):
        confirmed = "Confirmed", "CONFIRMED"
        cleared = "Cleared", "CLEARED"

    id = models.UUIDField(
        default=uuid.uuid4,
        primary_key=True,
        unique=True
    )
    name = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        help_text="Order name"
    )
    quantity = models.IntegerField(
        default=1,
        null=False,
        blank=False,
        help_text="Quantity of order placed"
    )
    order_owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        help_text="User who placed the order"
    )
    product = models.ForeignKey(
        Products,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        help_text="Product the user ordered"
    )
    short_code = models.CharField(
        max_length=6,
        blank=False,
        null=False,
        help_text="Confirmation code for order"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        help_text="Date order was created/placed"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text="Date order was modified"
    )

    class Meta:
        """
        Meta class that overrides django default model implementation
        """
        ordering = ['created_at']
        verbose_name = 'ORDER'
        verbose_name_plural = 'ORDERS'

    def gen_random_six_digit_code(self, length_of_code: int) -> str:
        all_digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        digits_holder = []
        for _ in range(length_of_code + 1):
            digits_holder.append(random.choice(all_digits))
        return "".join(digits_holder)

    def save(self, *args, **kwargs):
        if self.short_code == "":
            self.short_code = self.gen_random_six_digit_code(6)

        super(CustomUser, self).save()

    def __str__(self) -> str:
        return f"{self.order_owner.name} - {self.name}"
