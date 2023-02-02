from django.urls import path
from blog.views import BlogListView, BlogItemCreateView, BlogDetailView
urlpatterns = [
    path('', BlogListView.as_view(), name="list-view"),
    path('create/', BlogItemCreateView.as_view(), name="create-view"),
    path('detail/<int:pk>', BlogDetailView.as_view(), name="detail-view")
]