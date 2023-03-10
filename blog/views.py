from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from blog.models import BlogItem, BlogSetting


# Create your views here.

class AuthorRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        post_or_setting = self.get_object()
        return post_or_setting.author == self.request.user

class BlogListView(ListView):
    model = BlogItem
    context_object_name = 'blog_items' #Zodat ik geen 'object_list'  hoef te gebruiken in mijn template
    ordering = ("-date_created",)

    def get_queryset(self):
        username = self.kwargs.get('username')
        return BlogItem.objects.filter(author__username=username)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        popular_posts = BlogItem.objects.all().order_by('-views')
        username = self.kwargs.get('username')
        try:
            settings = BlogSetting.objects.get(author__username=username)
            context['settings'] = settings
        except BlogSetting.DoesNotExist:
            context['settings'] = None
            raise Http404
        if len(popular_posts) >= 3:
            context['popular_posts'] = popular_posts[:3]
        else:
            context['popular_posts'] = popular_posts
        return context


class BlogItemCreateView(LoginRequiredMixin, CreateView):
    model = BlogItem
    fields = ('title', 'text', 'visible',)
    login_url = "/login/"

    def get_success_url(self):
        username = self.kwargs['username']
        return reverse_lazy('list-view', kwargs={'username': username})

    def form_valid(self, form):
        #if the form is submitted, and valid. Make sure that the author is the logged in user
        form.instance.author = self.request.user
        return super().form_valid(form)


class BlogDetailView(DetailView):
    model = BlogItem
    fields = ('author', 'title', 'text',)
    context_object_name = "blog_post"

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        self.object.views += 1
        self.object.save()
        return response


class BlogUpdateView(AuthorRequiredMixin, UpdateView):
    model = BlogItem
    fields = ('title', 'text', 'visible',)

    def get_success_url(self):
        username = self.kwargs['username']
        return reverse_lazy('list-view', kwargs={'username': username})


class BlogItemDeleteView(AuthorRequiredMixin, DeleteView):
    model = BlogItem

    def get_success_url(self):
        username = self.kwargs['username']
        return reverse_lazy('list-view', kwargs={'username': username})


class BlogSettingsUpdateView(AuthorRequiredMixin, UpdateView):
    model = BlogSetting
    fields = ("blog_name", "about_me", "header_color", "post_color", "header_text_color", "post_color_text")

    def get_success_url(self):
        username = self.kwargs['username']
        return reverse_lazy('list-view', kwargs={'username': username})


