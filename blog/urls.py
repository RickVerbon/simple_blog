from django.urls import path
from blog.views import BlogListView, BlogItemCreateView, BlogDetailView
urlpatterns = [
    path('<str:username>/', BlogListView.as_view(), name="list-view"),
    path('<str:username>/create/', BlogItemCreateView.as_view(), name="create-view"),
    path('<str:username>/detail/<int:pk>', BlogDetailView.as_view(), name="detail-view")
]