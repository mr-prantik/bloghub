from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from .forms import *


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST['username']
            messages.success(request, f"Account Created for {username}")
            return HttpResponseRedirect(reverse("blog:blog-home"))

    else:
        form = UserRegisterForm()

    return render(request, "users/register.html", {
        "form": form
    })
