from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def user_login(request):
    """Render the login page.

    Parameters:
    request (HttpRequest): The request object.

    Returns:
    HttpResponse: The response object with the rendered template.
    """
    return render(request, 'authentication/login.html')

# Looking up in the Users table and returning an object that represents the logged-in user.
def authenticate_user(request):
    """Authenticate the user based on the username and password.

    Parameters:
    request (HttpRequest): The request object.

    Returns:
    HttpResponseRedirect: The response object that redirects to the contact page if the user is authenticated,
    or to the login page otherwise.
    """
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)   # If the user doesn’t exist in the table, this simply returns None.
    # Sending the user back to login if the object is None, and to a new HTML page otherwise.
    if user is None:
        return HttpResponseRedirect(
            reverse('user_auth:login')
    )
    else:
        login(request, user)
        return HttpResponseRedirect(
            reverse('band_app:contact')
    )

# Reading in the user data and sending it to (and renders) a new HTML file. 
def show_user(request):
    """Render the user page with the user data.

    Parameters:
    request (HttpRequest): The request object.

    Returns:
    HttpResponse: The response object with the rendered template and context data.
    """
    print(request.user.username)
    return render(request, 'authentication/user.html', {
        "username": request.user.username,
        "password": request.user.password
    })
