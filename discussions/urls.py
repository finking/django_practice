from django.urls import path
from .views import DiscussionDetailView, UserDiscussionListView, DiscussionCreateView, discussion_created


urlpatterns = [
    path('user/<str:username>/', UserDiscussionListView.as_view(), name='discussion-list'),
    path('new/', DiscussionCreateView.as_view(), name='discussion-create'),
    path('detail/<int:pk>/<slug:slug>', DiscussionDetailView.as_view(), name='discussion-detail'),
    path('create/', discussion_created, name='create')
]