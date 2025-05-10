from django.urls import path
from . import views

# chat_section/urls.py
urlpatterns = [
  path('',        views.room_list,        name='room_list'),
  path('random/', views.chat_rooms_redirect, name='chat_room_redirect'),
  path('<int:number>/', views.chat_rooms, name='chat_room'),
]

