from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, UpdateView
from blog.models import BlogItem, BlogSetting


# Create your views here.
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
        settings = BlogSetting.objects.get(author__username=username)
        context['settings'] = settings
        if len(popular_posts) >= 3:
            context['popular_posts'] = popular_posts[:3]
        else:
            context['popular_posts'] = popular_posts
        return context


class BlogItemCreateView(CreateView):
    model = BlogItem
    fields = ('title', 'text', 'visible',)

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


class BlogUpdateView(UpdateView):
    model = BlogItem
    fields = ('title', 'text', 'visible',)

    def get_success_url(self):
        username = self.kwargs['username']
        return reverse_lazy('list-view', kwargs={'username': username})


class BlogSettingsUpdateView(UpdateView):
    model = BlogSetting
    fields = ("blog_name", "about_me", "header_color", "post_color", "header_text_color", "post_color_text")

    def get_success_url(self):
        username = self.kwargs['username']
        return reverse_lazy('list-view', kwargs={'username': username})

