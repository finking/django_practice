from django.shortcuts import render

from django.views.generic import ListView, DetailView
from .models import Page


# Извлечение url по slug
class PageListView(ListView):
    paginate_by = 5
    model = Page
    template_name = 'getlink_app/slug_url/list_slug.html'


class PageDetailView(DetailView):
    model = Page
    template_name = 'getlink_app/slug_url/detail_slug.html'


##########
# Извлечение url по namespace
class PageListNamespace(ListView):
    model = Page
    template_name = 'getlink_app/ns/list_ns.html'


class PageDetailNamespace(DetailView):
    model = Page
    template_name = 'getlink_app/ns/detail_ns.html'


##########
# Извлечение url по AbsoluteUrl
class PageListGetAbsUrl(ListView):
    model = Page
    template_name = 'getlink_app/abs_url/list_abs_url.html'


class PageDetailGetAbsUrl(DetailView):
    model = Page
    template_name = 'getlink_app/abs_url/detail_abs_url.html'