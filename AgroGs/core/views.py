from django.views.generic import (
    TemplateView,
    DetailView
)
from AgroGs.products.models import Products
from AgroGs.cart.models import Cart, CartItem

class HomeView(TemplateView):
    template_name = "pages/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = Products.objects.all()
        return context

class ShopView(TemplateView):
    template_name = "pages/shop.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = Products.objects.all()
        return context

class ProductDetailView(DetailView):
    model = Products
    template_name = "pages/product_detail.html"


def cart(request):
    cart = Cart.objects.filter(user=request.user.pk).first()
    cart_items_count = CartItem.objects.filter(cart=cart).count()
    cart_items = CartItem.objects.filter(cart=cart)
    context = {"cart_items_count": cart_items_count, "items": cart_items, "cart": cart}
    return context
    
    