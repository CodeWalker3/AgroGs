from allauth.account.forms import SignupForm
from django import forms
from .models import User
from django.contrib.auth.models import Group
class SimpleSignupForm(SignupForm):
    profile_pic = forms.ImageField(required=False)
    def save(self, request):
        user = super(SimpleSignupForm, self).save(request)

        user.save()
        return user
    

class UpdateUserForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ['username', 'email', 'cnpj']
    
    def __init__(self, *args, **kwargs):
        super(UpdateUserForm, self).__init__(*args, **kwargs)
        self.is_vendor = kwargs['initial']['is_vendor']

    def save(self, commit=True):
        obj = super(UpdateUserForm, self).save(False)
        group = Group.objects.get(name="vendor")
        obj.groups.add(group)
        obj.is_vendor = True
        commit and obj.save()
        return obj