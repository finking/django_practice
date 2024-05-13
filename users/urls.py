from django.urls import path
from . import views

urlpatterns = [
    path('public-profile/<str:username>/', views.public_profile,  name='public-profile'),
]