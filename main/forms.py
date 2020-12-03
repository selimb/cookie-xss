from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Post
from django.contrib.auth import get_user, get_user_model

User = get_user_model()


class PostForm(forms.models.ModelForm):
    class Meta:
        model = Post
        fields = ("content",)

    def save(self, user):
        self.instance.user = user
        return super().save()


class DummyAuthenticationForm(AuthenticationForm):
    password = None

    def clean(self):
        return self.cleaned_data

    def get_user(self):
        username = self.cleaned_data.get("username")
        user, _ = User.objects.get_or_create(username=username)
        print("get_user", user)
        return user
