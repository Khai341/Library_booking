from django.contrib import admin

from .models import Users, BookingHistory
# Register your models here.
admin.site.register(Users)
admin.site.register(BookingHistory)