from allauth.account.forms import SignupForm
from django import forms
from .models import User

class SimpleSignupForm(SignupForm):
    profile_pic = forms.ImageField()
    def save(self, request):
        user = super(SimpleSignupForm, self).save(request)
        user.cnpj = self.cleaned_data['cnpj']
        user.save()
        return user