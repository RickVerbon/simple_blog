from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import ListView, FormView
from users.forms import LoginForm, RegisterForm
from django.contrib.auth import login, authenticate


# Create your views here.
class UserListView(ListView):
    model = User
    fields = ("username",)
    context_object_name = "users"
    template_name = "users/user_list.html"


class LoginView(FormView):
    form_class = LoginForm
    success_url = "/"
    template_name = 'users/login.html'

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return super().form_valid(form)


class RegisterView(FormView):
    form_class = RegisterForm
    success_url = "/"
    template_name = 'users/register.html'

    def form_valid(self, form):
        form.save()
        user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
        login(self.request, user)
        return super().form_valid(form)