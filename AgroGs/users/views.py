from django.shortcuts import render
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from django.contrib import messages

from AgroGs.users.forms import UpdateUserForm
from .models import User
# Create your views here.

class Home(TemplateView):
    template_name = 'home.html'

class UserVendorUpdateView(UpdateView):
    model = User
    template_name = "user_change_form.html"
    form_class= UpdateUserForm
    success_url = reverse_lazy('home')
    def get_initial(self):
        self.initial.update({ 'is_vendor': True })
        return self.initial
    def get_object(self):
        return self.request.user

   
       
   
