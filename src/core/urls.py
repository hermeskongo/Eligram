from django.contrib import admin
from django.urls import path

from core import views
from core.views import IndexView, DeletePost, LikeView

app_name = "core"

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('delete/<uuid:id>', DeletePost.as_view(), name="delete"),
    path('like/<uuid:post_id>/', LikeView.as_view(), name="like")
]
