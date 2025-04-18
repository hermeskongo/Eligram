from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView, LogoutView

# Create your views here.
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, UpdateView

from accounts.forms import RegistrationForm, UserLoginForm, UserSettingForm
from accounts.models import Profile
from utils.mixins import CustomLoginRequiredMixin


class RegistrationView(CreateView):
    form_class = RegistrationForm
    model = get_user_model()
    template_name = "signup.html"
    success_url = reverse_lazy("core:index")
    
    def form_valid(self, form):
        user = form.save()
        Profile.objects.create(user=user)
        return super(RegistrationView, self).form_valid(form)


class UserLoginView(LoginView):
    next_page = reverse_lazy("core:index")
    form_class = UserLoginForm
    template_name = 'signin.html'


class UserLogoutView(LogoutView):
    next_page = reverse_lazy("accounts:login")


class UserSettingView(UpdateView):
    template_name = 'setting.html'
    model = Profile
    form_class = UserSettingForm
    success_url = reverse_lazy("core:index")
    
    
    