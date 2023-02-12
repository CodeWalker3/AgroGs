from django.views.generic import (
    TemplateView,
    DetailView,
)
from django.shortcuts import render, redirect
from AgroGs.products.models import Products
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from cart.cart import Cart



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


@login_required
def cart_add(request, id):
    cart = Cart(request)
    product = Products.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart")


@login_required
def item_clear(request, id):
    cart = Cart(request)
    product = Products.objects.get(id=id)
    cart.remove(product)
    return redirect("cart")


@login_required
def item_increment(request, id):
    cart = Cart(request)
    product = Products.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart")


@login_required
def item_decrement(request, id):
    cart = Cart(request)
    product = Products.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart")


@login_required
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart")


@login_required
def cart_detail(request):
    return render(request, 'pages/cart.html')