from django.contrib import admin
from django.urls import path

from accounts.views import RegistrationView, UserLoginView, UserLogoutView
from core import views

app_name = "accounts"

urlpatterns = [
    path('register/', RegistrationView.as_view(),name="registration"),
    path('login/', UserLoginView.as_view(), name="login"),
    path('logout/', UserLogoutView.as_view(), name="logout")
]
