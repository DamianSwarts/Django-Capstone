from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

# Create your views here.
class signup(generic.CreateView):
    """A class-based view to handle user registration.

    Attributes:
    form_class (UserCreationForm): The form class to use for creating new users.
    success_url (str): The URL to redirect to after successful registration.
    template_name (str): The name of the template to render the registration form.
    """
    form_class = UserCreationForm
    success_url = reverse_lazy("user_auth:login")
    template_name = "registration/signup.html"
