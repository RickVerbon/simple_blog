from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import ListView, FormView
from users.forms import LoginForm, RegisterForm
from django.contrib.auth import login, authenticate
from blog.models import BlogSetting, BlogItem


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
        blog_setting = BlogSetting.objects.create(author=user)
        blog_item = BlogItem.objects.create(author=user, title="This is my first BlogPost", text="See title", visible=True)
        login(self.request, user)
        return super().form_valid(form)