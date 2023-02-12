from django import forms
from django.forms import ModelForm

from .models import Products, Category


class ProductsForm(ModelForm):
    class Meta:
        model = Products
        fields = ["name", "price", "quantity", "category", "image", "description"]

    def __init__(self, *args, **kwargs):
        super(ProductsForm, self).__init__(*args, **kwargs)
        self.created_by = kwargs['initial']['created_by']

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    def save(self, commit=True):
        obj = super(ProductsForm, self).save(False)
        obj.created_by = self.created_by
        commit and obj.save()
        return obj

    
        

    
        
    