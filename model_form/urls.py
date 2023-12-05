from django.urls import path
from .views import AuthorDetailView, author_created


urlpatterns = [
    path('create/', author_created, name='author-create'),
    path('<int:pk>/detail/', AuthorDetailView.as_view(), name='author-detail')
]