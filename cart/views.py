from urllib import response
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from stripe import Product

from cart.cart import Cart
from shop.models import ProductProxy


def cart_view(request):
    cart = Cart(request)
    return render(request, "cart/cart-view.html")


def cart_add(request): 
    cart = Cart(request)

    if request.POST.get("action") == "post":
        product_id = int(request.POST.get("product_id"))
        product_qty = int(request.POST.get("product_qty"))

        product = get_object_or_404(ProductProxy, id=product_id)

        cart.add(product= product, quantity = product_qty)

        cart_qty = cart.__len__()

        response = JsonResponse({"qty": cart_qty, 'product': product.title})

        return response

def cart_delete(request): ...


def cart_update(request): ...
