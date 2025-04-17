from django.contrib import admin

# Register your models here.
from core.models import Posts


@admin.register(Posts)
class PostsAdmin(admin.ModelAdmin):
    pass
