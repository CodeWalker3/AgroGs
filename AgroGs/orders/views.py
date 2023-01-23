from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView, UpdateView, ListView
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from .models import Orders
from .filters import OrdersFilter


class OrdersList(LoginRequiredMixin, ListView):
    model = Orders
    queryset = Orders.objects.all()
    paginate_by = 4
    filterset_class = OrdersFilter
    template_name= "orders.html"

    def get_queryset(self):
        queryset = super().get_queryset().filter(client=self.request.user)
        self.filterset = self.filterset_class(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form_filter"] = self.filterset.form
        return context