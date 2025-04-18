from django.contrib import admin

# Register your models here.
from core.models import Posts, Likes


@admin.register(Posts)
class PostsAdmin(admin.ModelAdmin):
    pass


@admin.register(Likes)
class LikesAdmin(admin.ModelAdmin):
    pass
