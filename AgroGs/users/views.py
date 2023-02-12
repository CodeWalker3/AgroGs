from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from django.contrib import messages

from AgroGs.users.forms import ProfileUpdateForm, UpdateUserForm
from .models import User, UserProfile
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

@login_required
def profile(request):
    if request.method == 'POST':
        p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if p_form.is_valid():
            p_form.save()
            messages.success(request,'Your Profile has been updated!')
            return redirect('home')
    else:
        p_form = ProfileUpdateForm(instance=request.user)
    context={'p_form': p_form}
    return render(request, 'test.html',context )

   
    
