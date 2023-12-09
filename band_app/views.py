from django.shortcuts import render, redirect
from .models import BandMember, ContactInfo
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


# Create your views here.
@login_required(login_url="user_auth:login")
def home(request): # Get the band members from the database
    """Render the home page with the band members.

    Parameters:
    request (HttpRequest): The request object.

    Returns:
    HttpResponse: The response object with the rendered template and context data.
    """
    band_members = BandMember.objects.all()
    # Render the home.html template with the context data 
    return render(request, 'home.html', {'band_members': band_members})

def contact(request):
    """Render the contact page with the contact info.

    Parameters:
    request (HttpRequest): The request object.

    Returns:
    HttpResponse: The response object with the rendered template and context data.
    """
    # Get the contact info from the database
    contact_info = ContactInfo.objects.first()
    # Render the contact.html template with the context data
    return render(request, 'contact.html', {'contact_info': contact_info})

def logout(request):
    """Log out the user and redirect to the login page.

    Parameters:
    request (HttpRequest): The request object.

    Returns:
    HttpResponseRedirect: The response object that redirects to the login page.
    """
    logout(request) # log out the user
    return redirect("user_auth:login") # redirect to home page
