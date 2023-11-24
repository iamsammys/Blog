from django.urls import path
from . import views
from .views import (
    PostListView,
    PostCreateView,
    PostDetailView,
    PostUpdateView,
    PostDeleteView,
)

app_name = 'blog_app'

urlpatterns = [
    path('', PostListView.as_view(), name="index"),
    path('about/', views.about, name="about"),
    path('new/', PostCreateView.as_view(), name="post-create"),
    path('post/<str:pk>/', PostDetailView.as_view(), name="post-detail"),
    path('post/<str:pk>/update/', PostUpdateView.as_view(), name="post-update"),
    path('post/<str:pk>/delete/', PostDeleteView.as_view(), name="post-delete")
    ]