from django.urls import path
from .views import PageListView, PageDetailView, PageListNamespace, PageDetailNamespace, PageListGetAbsUrl, PageDetailGetAbsUrl


urlpatterns = [
    path('slug/', PageListView.as_view(), name='sluglist'),
    path('slug/<slug>/', PageDetailView.as_view(), name='slug-detail'),

    #namespace
    path('ns/', PageListNamespace.as_view(), name='view_list_ns'),
    path('ns/<int:pk>/detail/', PageDetailNamespace.as_view(), name='view_detail_ns'),

    # get_absolute_url
    path('absolute/list/', PageListGetAbsUrl.as_view(), name='list_url'),
    path('absolute/<int:id>/', PageDetailGetAbsUrl.as_view(), name='detail_url'),
]