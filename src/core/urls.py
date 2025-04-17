from django.contrib import admin
from django.urls import path

from core import views
from core.views import IndexView, DeletePost

app_name = "core"

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('delete/<uuid:id>', DeletePost.as_view(), name="delete")
]
