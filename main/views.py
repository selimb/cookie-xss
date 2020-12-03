import django.contrib.auth.views
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse
from django.http.request import HttpRequest
from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm, DummyAuthenticationForm


@login_required
def index(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save(user=request.user)
            return redirect("index")
    else:
        form = PostForm()
    posts = Post.objects.all()
    return render(request, "index.html", {"form": form, "posts": posts})


class DummyLoginView(django.contrib.auth.views.LoginView):
    form_class = DummyAuthenticationForm


class LogoutView(django.contrib.auth.views.LogoutView):
    next_page = "login"