from django_filters import FilterSet, CharFilter
from django import forms
from .models import Orders



class OrdersFilter(FilterSet):
    name = CharFilter(
        lookup_expr="icontains", widget=forms.TextInput(attrs={"class":"form-control"})
    )

    class Meta:
        model = Orders
        fields = ["name"]