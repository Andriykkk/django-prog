from django.urls import path

from shop.views import category_list, products_detail_view

from .views import (
    cart_add,
    cart_view,
)

app_name = "cart"

urlpatterns = [
    path("", cart_view, name="cart-view"),
    path("add/", cart_add, name="add_to_cart"),
]
