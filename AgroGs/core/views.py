from django.views.generic import (
    TemplateView,
    DetailView
)
from AgroGs.products.models import Products
from AgroGs.cart.models import CartItem, Cart

class HomeView(TemplateView):
    template_name = "pages/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = Products.objects.all()
        if Cart.objects.exists():
            cart = Cart.objects.filter(user=self.request.user).first()
            context['cart_items'] = CartItem.objects.filter(cart=cart).count()
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
