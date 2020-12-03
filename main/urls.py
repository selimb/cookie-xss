from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.DummyLoginView.as_view(), name="login"),
    path("logout", views.LogoutView.as_view(), name="logout"),
]
