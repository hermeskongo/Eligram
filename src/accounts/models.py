from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.

user = get_user_model()

class Profile(models.Model):
    user = models.OneToOneField(user, models.CASCADE)
    bio = models.TextField()
    img = models.ImageField(verbose_name='Photo de profil', upload_to="profile")
    location = models.CharField(max_length=100, blank=True)
    
    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name = 'Profil'
        