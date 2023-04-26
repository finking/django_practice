from django.shortcuts import render
from django.views.generic import ListView
from .models import Sites


class SitesListView(ListView):
    model = Sites
    template_name = 'info_notes/sites/sites_list.html'

    # queryset = Sites.objects.filter(date_added__year=2023)
    #
    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     return queryset.order_by('name').order_by('-date_added').reverse()[:2]

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context["sites_context_all_list"] = Sites.objects.all()
        return context