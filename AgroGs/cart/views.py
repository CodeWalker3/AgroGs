from django.shortcuts import render
from django.db.models import F, Sum
from django.views import View
from django.shortcuts import redirect
from .models import Cart, CartItem
from AgroGs.products.models import Products
# Create your views here.
class CartView(View):
    def get(self, request):
        if Cart.objects.exists():
            cart = Cart.objects.annotate(
                price=Sum(F('cartitem__total'))
            ).get(
                user=request.user
            )
            cart.total = cart.price
            cart.save()
            cart_items = CartItem.objects.filter(cart=cart)
            return render(
                request, 'cart_test.html',{
                    'cart':cart,
                    'cart_items': cart_items
                }
            )
        else:
            return render(request, "cart_test.html")
        # …

def cart_add(request, pk):
    product = Products.objects.get(pk=pk)
    if Cart.objects.exists():
        cart = Cart.objects.get(user=request.user)
        if  CartItem.objects.filter(cart=cart).exists() and CartItem.objects.filter(product=product).exists():
            CartItem.objects.filter(product=product).update(quantity=F('quantity') + 1)
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

    return redirect("home")