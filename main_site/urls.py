from django.urls.conf import re_path, path
from .views import ArticleListView, ArticleDetailView


urlpatterns = [
    re_path(r'^$', ArticleListView.as_view(), name='list'),
    path('<str:slug>/', ArticleDetailView.as_view(), name='article-detail'),
]