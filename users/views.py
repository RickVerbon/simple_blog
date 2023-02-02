from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import ListView


# Create your views here.
class UserListView(ListView):
    model = User
    fields = ("username",)
    context_object_name = "users"
    template_name = "users/user_list.html"
