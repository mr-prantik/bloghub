from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from .forms import *
from django.contrib.auth.decorators import login_required
from .models import *
from  blog.models import *

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
    return render(request, "users/profile.html")
    # return HttpResponseRedirect(reverse("users:users-login"))
    

@login_required
def update_profile(request):
    if request.method=="POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return HttpResponseRedirect(reverse("users:users-profile"))
        else:
            u_form = UserUpdateForm(instance=request.user)
            p_form=ProfileUpdateForm(instance=request.user.profile)
    u_form = UserUpdateForm(instance=request.user)
    p_form = ProfileUpdateForm(instance=request.user.profile)
    return render(request, "users/update_profile.html", {
        "u_form" : u_form,
        "p_form" : p_form
    })

@login_required
def my_posts(request):
    return render(request, "users/my_posts.html")