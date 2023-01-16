from django_filters import FilterSet, CharFilter, ModelChoiceFilter
from django import forms
from .models import Products, Category



class ProductsFilter(FilterSet):
    name = CharFilter(
        lookup_expr="icontains", widget=forms.TextInput(attrs={"class":"form-control"})
    )
    description = CharFilter(
        lookup_expr="icontains", widget=forms.TextInput(attrs={"class": "form-control"})
    )
    category = ModelChoiceFilter(
        queryset=Category.objects.all())

    class Meta:
        model = Products
        fields = ["name", "description", "category"]