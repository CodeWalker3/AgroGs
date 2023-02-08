from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    UpdateView, 
    ListView,
    DeleteView,
    DetailView
)
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.views import View
from .filters import ProductsFilter
from .forms import ProductsForm
from .models import (
    Category, 
    Products
)
# Create your views here.
class CreateCategory(CreateView):
    pass

class ProductsList(ListView):
    model = Products
    paginate_by = 4
    filterset_class = ProductsFilter

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = self.filterset_class(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form_filter"] = self.filterset.form
        context["object_list"] = Products.objects.filter(created_by=self.request.user).all()

        return context


class ProductsDetail(DetailView):
    model = Products

class ProductsUserMixin(LoginRequiredMixin, UserPassesTestMixin):

    def test_func(self):
        return self.request.user.has_perm('Can add Products')

    def handle_no_permission(self):
        return redirect(reverse_lazy('products:list'))

class CreateProduct(ProductsUserMixin ,CreateView):
    model = Products
    form_class = ProductsForm
    success_url = reverse_lazy("products:list")
    def get_initial(self):
        self.initial.update({ 'created_by': self.request.user })
        return self.initial

class UpdateProduct(UpdateView):
    model = Products
    form_class = ProductsForm
    success_url = reverse_lazy("products:list")
    def get_initial(self):
        self.initial.update({ 'created_by': self.request.user })
        return self.initial

class DeleteProduct(DeleteView):
    model = Products
    success_url = reverse_lazy("products:list")
    
    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)

class UpdateCategory(UpdateView):
    pass

