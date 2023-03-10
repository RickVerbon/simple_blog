from django.urls import path
from blog.views import BlogListView, BlogItemCreateView, BlogDetailView, BlogUpdateView, BlogSettingsUpdateView, \
    BlogItemDeleteView

urlpatterns = [
    path('<str:username>/', BlogListView.as_view(), name="list-view"),
    path('<str:username>/create/', BlogItemCreateView.as_view(), name="create-view"),
    path('<str:username>/detail/<int:pk>', BlogDetailView.as_view(), name="detail-view"),
    path('<str:username>/update/<int:pk>', BlogUpdateView.as_view(), name="update-view"),
    path('<str:username>/delete/<int:pk>', BlogItemDeleteView.as_view(), name='delete-view'),
    path('<str:username>/settings/<int:pk>/', BlogSettingsUpdateView.as_view(), name="settings-update-view"),
]