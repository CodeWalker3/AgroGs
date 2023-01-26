from django.views.generic import (
    TemplateView,
    DetailView,
)
from AgroGs.products.models import Products
from django.contrib.auth.mixins import LoginRequiredMixin

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


class CheckoutView(LoginRequiredMixin, TemplateView):
    template_name = "pages/checkout.html"

    
    