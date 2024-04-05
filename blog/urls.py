from django.urls import path
from .views import UserPostListView, PostCreateView, post_detail_view, PostDeleteView, PostUpdateView, index, \
    HomePostListViewAllUsers, all_save_view_posts, save_post_is_ajax


urlpatterns = [
    path("", index, name="index-home"),
    path("home/", HomePostListViewAllUsers.as_view(), name="blog-home"),
    path('post/user/<str:username>/', UserPostListView.as_view(), name='user-posts-list'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/save/', save_post_is_ajax, name='post-save'),
    path('post/delete/<int:pk>/', PostDeleteView.as_view(), name='post-delete'),
    path('post/update/<int:pk>/', PostUpdateView.as_view(), name='post-update'),
    # path('post/detail/<int:pk>/<slug:slug>', PostDetailView.as_view(), name='post-detail'),
    path('saved_posts', all_save_view_posts, name='saved_posts'),
    path('post/detail/<int:pk>', post_detail_view, name='post-detail'),
]