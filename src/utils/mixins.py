from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin


class CustomLoginRequiredMixin(LoginRequiredMixin):
    """
    Mixin permettant d'afficher un message d'erreur à l'utilisateur s'il n'est pas connecté
    """
    permission_denied_message = "Vous devez être connecté pour accéder à cette page !"
    
    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            messages.error(self.request, self.permission_denied_message);
            self.handle_no_permission()
        return super(CustomLoginRequiredMixin, self).dispatch(*args, **kwargs)
