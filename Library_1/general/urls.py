from django.urls import path
from . import views

app_name = 'general'

urlpatterns = [
    path('', views.ReturnMain),
    path('Booking', views.Booking),
    path('Ajax0', views.Ajax0), #, name='ajax-view'
    path('Ajax1', views.Ajax1),
    path('Ajax2', views.Ajax2),
]