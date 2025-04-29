from django.urls import path
from . import views

app_name = 'librarianAdmin'

urlpatterns = [
    path('booking-history/', views.booking_history, name='booking_history'),
    path('', views.return_main),
    path('booking-detail/<int:booking_id>/', views.booking_detail, name='booking_detail'),  # ← comma added here
    path('cancel-booking/<int:booking_id>/', views.cancel_booking, name='cancel_booking'),
    path('send-invitation/<int:booking_id>/', views.send_invitation, name='send_invitation'),
    path('rebook/<int:booking_id>/', views.rebook, name='rebook'),
    path('delete-invitation/<str:datetime_str>/', views.delete_invitation, name='delete_invitation'),
    path('accept-invitation/<str:datetime_str>/', views.accept_invitation, name='accept_invitation'),
]
