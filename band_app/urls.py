from django.urls import path 
from . import views

app_name = 'band_app'
urlpatterns = [ 
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path("logout/", views.logout, name="logout"),

]