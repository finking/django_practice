from django.urls import path
from .views import UserPostListView, PostCreateView, PostDetailView, PostDeleteView, PostUpdateView, index


urlpatterns = [
    path("", index, name="index-home"),
    path('post/user/<str:username>/', UserPostListView.as_view(), name='user-posts-list'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/delete/<int:pk>/', PostDeleteView.as_view(), name='post-delete'),
    path('post/update/<int:pk>/', PostUpdateView.as_view(), name='post-update'),
    # path('post/detail/<int:pk>/<slug:slug>', PostDetailView.as_view(), name='post-detail'),
    path('post/detail/<int:pk>', PostDetailView, name='post-detail'),
]