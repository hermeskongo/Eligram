from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView

from core.forms import PostsForm
from core.models import Posts


class IndexView(CreateView):
    template_name = 'index.html'
    form_class = PostsForm
    model = Posts
    success_url = reverse_lazy("core:index")
    
    def form_valid(self, form):
        post = form.save(commit=False)
        post.user = self.request.user
        post.save()
        return super(IndexView, self).form_valid(form)

    def get_context_data(self, *args, **kwargs):
        # Ajout des posts dans le context parent
        
        context = super(IndexView, self).get_context_data(*args, **kwargs)
        
        posts = Posts.objects.all().order_by("-created_at")
        
        context['posts'] = posts
        
        return context
        
        
class DeletePost(DeleteView):
    model = Posts
    success_url = reverse_lazy("core:index")
    
    def get_object(self, *args, **kwargs):
        uuid = self.kwargs['id']
        
        post = Posts.objects.filter(id=uuid)
        return post
    