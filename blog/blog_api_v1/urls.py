from django.urls import path
from . import views


urlpatterns = [
    path('posts/', views.PostListApiView.as_view(), name="post_api-list"),
    path('posts/create/', views.PostCreateApiView.as_view(), name="post_api-create")
]