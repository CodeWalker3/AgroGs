from django.shortcuts import render
from django.db.models import F, Sum
from django.views import View
from .models import Cart
# Create your views here.
class CartView(View):
    def get(self, request):
        cart = Cart.objects.annotate(
            price=Sum(F('cartitem__total'))
        ).get(
            user=request.user
        )
        cart.total = cart.price
        cart.save()
        return render(
            request, 'cart_test.html',{
                'cart':cart
            }
        )
        # …
    