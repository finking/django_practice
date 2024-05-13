from django.shortcuts import render
from django.contrib.auth.models import User


def public_profile(request, username):
    user = User.objects.get(username=username)
    return render(request, 'users/public_profile.html', {'public_user': user})


# Create your views here.
