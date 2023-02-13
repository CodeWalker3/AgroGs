from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from cart.context_processor import cart_total_amount
from AgroGs.products.models import Products
from AgroGs.users.forms import AddressForm
from .models import Orders, ProductOrder
from .filters import OrdersFilter
from AgroGs.users.models import Address
from cart.cart import Cart


class OrdersListView(LoginRequiredMixin, ListView):
    model = Orders
    paginate_by = 4
    filterset_class = OrdersFilter

    def get_queryset(self):
        queryset = super().get_queryset().filter(user=self.request.user)
        self.filterset = self.filterset_class(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form_filter"] = self.filterset.form
        self.object_list = self.get_queryset()
        context["object_list"] = Orders.objects.filter(user=self.request.user).all()
        return context


class OrdersCreateView(LoginRequiredMixin, View):
    form_class = AddressForm
    template_name = "orders/checkout.html"

    def get(self, request):
        if Address.objects.filter(user=request.user).exists():
            return render(request, self.template_name)
        else:
            form = self.form_class(request.POST)
            return render(request, self.template_name, {'form': form})

    def post(self, request):
        cart = Cart(request)
        if Address.objects.filter(user=request.user).exists():
            order = Orders.objects.create(user=request.user)
            self.create_product_orders(order, cart)
            cart.clear()
            return redirect('orders:list')
        else:
            form = self.form_class(request.POST)
            if form.is_valid():
                form.instance.user = self.request.user
                form.save()
                order = Orders.objects.create(user=request.user)
                self.create_product_orders(order, cart)
                cart.clear()
                return redirect('orders:list')

    def create_product_orders(self, order, cart):
        for i, item in cart.cart.items():
            product = Products.objects.filter(id=item['product_id']).first()
            product_order = ProductOrder.objects.create(
                order=order,
                product=product,
                quantity=item['quantity']
            )
            product.quantity = int(product.quantity) - int(item['quantity'])
            product.save()
            product_order.save()
        order.total = cart_total_amount(self.request)["cart_total_amount"]  
        order.save()

        