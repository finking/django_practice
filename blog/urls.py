from django.urls import path
from .views import UserPostListView, PostCreateView, PostDetailView, index


urlpatterns = [
    path("", index, name="index-home"),
    path('post/user/<str:username>/', UserPostListView.as_view(), name='user-posts-list'),
    path('post/new', PostCreateView.as_view(), name='post-create'),
    path('post/detail/<int:pk>/<slug:slug>', PostDetailView.as_view(), name='post-detail')
]