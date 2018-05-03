from django import forms
from django.forms import ModelForm
from django.contrib.auth import authenticate, get_user_model, login, logout
from .models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

User = get_user_model()


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("Wrong credentials")
            if not user.check_password(password):
                raise forms.ValidationError("Incorrect password")
            if not user.is_active:
                raise forms.ValidationError("User disabled")
        return super(LoginForm, self).clean(*args, **kwargs)

