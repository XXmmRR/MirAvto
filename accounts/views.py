from .forms import CustomUserCreationForm, LoginUserForm
from django.urls import reverse_lazy
from django.views import generic
from catalog.models import PartList
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm


class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    extra_context = {PartList.objects.all(): 'parts'}
    success_url = reverse_lazy('login')
    template_name = 'registration/registration.html'


class LoginView(LoginView):
    form_class = LoginUserForm
    template_name = 'registration/login.html'
