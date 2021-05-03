from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

#import models
from .models import User
# Create your views here.

# register
def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
    
        # Password confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "users/register.html", {
                "message": "Password must match."
            })
        
        # Create new user
        try: 
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "users/register.html",{
                "message": "Username already taken."
            })
        login(request,user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "../templates/users/register.html")


def login_view(request):
    if request.method == "POST":
        # Sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check the authentication
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "../templates/users/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "../templates/users/login.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))
