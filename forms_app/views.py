from django.http import request
from django.shortcuts import render
from .forms import ContactForm


def contact_send(request):
    if request.method == "POST":
        form = ContactForm(request.POST, request.FILES)
    else:
        form = ContactForm()
