from allauth.account.forms import SignupForm
from django import forms
from .models import User

class SimpleSignupForm(SignupForm):
    phone = forms.CharField(max_length=12, label='Телефон')
    def save(self, request):
        user = super(SimpleSignupForm, self).save(request)
        user.cnpj = self.cleaned_data['cnpj']
        user.save()
        return user