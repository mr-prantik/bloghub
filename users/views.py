from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from .forms import *
from django.contrib.auth.decorators import login_required
from .models import *

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST['username']
            messages.success(request, f"Account Created for {username}")
            return HttpResponseRedirect(reverse("users:users-login"))

    else:
        form = UserRegisterForm()

    return render(request, "users/register.html", {
        "form": form
    })

@login_required
def profile(request):
    # if request.user.is_authenticated:
    # messages.error(request, f"You need to login first")
    return render(request, "users/profile.html", {
        "profile" : Profile.objects.all()
    })
    # return HttpResponseRedirect(reverse("users:users-login"))
    pass