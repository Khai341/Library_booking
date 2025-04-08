from django.urls import path
from . import views

app_name = 'librarianAdmin'

urlpatterns = [
    path('', views.ReturnMain),
]