import uuid

from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.

user = get_user_model()


class Posts(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4())
    user = models.ForeignKey(user, on_delete=models.CASCADE, related_name="posts", verbose_name="Utilisateur")
    image = models.ImageField(upload_to="posts", )
    caption = models.TextField(verbose_name="Légende")
    created_at = models.DateTimeField(auto_now_add=True)
    n_of_likes = models.IntegerField(default=0)
    
    def __str__(self):
        return f"Publication de {self.user.username}"
    
    class Meta:
        verbose_name = 'Publication'


class Likes(models.Model):
    post = models.ForeignKey(Posts, related_name="likes", on_delete=models.CASCADE)
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Like de {self.user.username} pour {self.post}"
    
    class Meta:
        verbose_name = "Like"
        unique_together = ('post', 'user')
