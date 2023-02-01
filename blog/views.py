from django.shortcuts import render
from django.views.generic import DetailView, ListView
from blog.models import BlogItem


# Create your views here.
class BlogListView(ListView):
    model = BlogItem
    context_object_name = 'blog_items' #Zodat ik geen 'object_list'  hoef te gebruiken in mijn template

