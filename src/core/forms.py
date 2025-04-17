from django import forms

from core.models import Posts


class PostsForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ('image', 'caption')
        