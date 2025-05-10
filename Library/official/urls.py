from django.urls import path
from . import views

urlpatterns = [
    path('', views.official_list, name = 'official_list'),
]