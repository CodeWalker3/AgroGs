from django.shortcuts import render
from django.db.models import F, Sum
from django.views import View
from django.shortcuts import redirect
from .models import Cart, CartItem
from AgroGs.products.models import Products
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
# Create your views here.
class CartView(LoginRequiredMixin, View):
    def get(self, request):
        if CartItem.objects.exists():
            cart = Cart.objects.annotate(
                price=Sum(F('cartitem__total'))
            ).get(
                user=request.user
            )
            cart.total = cart.price
            cart.save()
            cart_items = CartItem.objects.filter(cart=cart)
            return render(
                request, 'cart.html',{
                    'cart':cart,
                    'cart_items': cart_items
                }
            )
        else:
            cart = Cart.objects.filter(user=request.user)
            cart.delete()
            return render(request, "cart.html")
        # …
@login_required
def cart_add(request, pk):
    product = Products.objects.get(pk=pk)
    if Cart.objects.exists():
        cart = Cart.objects.get(user=request.user.pk)
        if  CartItem.objects.filter(cart=cart).exists() and CartItem.objects.filter(product=product).exists():
            CartItem.objects.filter(product=product).update(quantity=F('quantity') + 1, total=float(product.price) * (F('quantity') + 1))
        else:
            cart_item = CartItem.objects.create(
                cart=cart,
                product=product,
            )
            cart_item.save()
    else:
        cart = Cart.objects.create(user=request.user)
        cart.save()
        cart_item = CartItem.objects.create(
            cart=cart,
            product=product,
        )
        cart_item.save()

    return redirect("cart")


def remove_item(request, pk):
    product = Products.objects.get(pk=pk)
    cart = Cart.objects.get(user=request.user.pk)
    cart_item = CartItem.objects.filter(cart=cart, product=product)
    cart_item.delete()
    return redirect("cart")

def cart(request):
    cart = Cart.objects.filter(user=request.user.pk).first()
    cart_items_count = CartItem.objects.filter(cart=cart).count()
    cart_items = CartItem.objects.filter(cart=cart)
    context = {"cart_items_count": cart_items_count, "cart_items": cart_items, "cart": cart}
    return context