from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm
from django.contrib.auth import views as auth_views

class SignUpView(CreateView):
    template_name = "registration/signup.html"
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")  

class CustomLoginView(auth_views.LoginView):
    template_name = 'registration/login.html'
    success_url = reverse_lazy('home')

class CustomLogoutView(auth_views.LogoutView):
    next_page = reverse_lazy('home')

class CustomPasswordChangeView(auth_views.PasswordChangeView):
    success_url = reverse_lazy('home')
    template_name = 'registration/password_change.html'

class CustomPasswordResetView(auth_views.PasswordResetView):
    email_template_name = 'registration/password_reset_email.html'
    success_url = reverse_lazy('password_reset_done')
    template_name = 'registration/password_reset.html'
