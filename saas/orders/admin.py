from django.contrib import admin
from .models import Orders
from django.conf import settings
from products.models import Products


@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    """
    Custom orders admin panel
    """
    list_display = ("get_ordered_product_owner", "get_ordered_product_name", "get_order_placer", "get_number_of_orders_for_a_product")

    def get_ordered_product_owner(self, obj) -> str:
        """
        Name of user who owns the product that was ordered
        """
        product_owner_name = obj.product.owner.name
        return product_owner_name

    def get_ordered_product_name(self, obj) -> str:
        """
        Name of product that was ordered
        """
        product_name = obj.product.name
        return product_name

    def get_order_placer(self, obj) -> str:
        """
        Name of user who placed the order
        """
        user_who_placed_order = obj.order_owner.name
        return user_who_placed_order

    def get_number_of_orders_for_a_product(self, obj) -> int:
        """
        Number of orders placed for a product
        """
        number_of_orders_for_a_product = obj.filter(order_owner=settings.AUTH_USER_MODEL,
                                                    product=Products).count()
        return number_of_orders_for_a_product

    get_ordered_product_owner.short_description = "product owner"
    get_ordered_product_name.short_description = "product name"
    get_order_placer.short_description = "order placer"
    get_number_of_orders_for_a_product.short_description = "number of orders"
