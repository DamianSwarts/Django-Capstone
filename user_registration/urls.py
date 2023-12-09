from django.urls import path
from .views import signup

app_name = 'user_registration'
urlpatterns = [
    path("signup/", signup.as_view(), name="signup"),
]