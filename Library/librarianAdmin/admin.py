from django.contrib import admin

from .models import Users, BookingHistory, Invitation
# Register your models here.
admin.site.register(Users)
admin.site.register(BookingHistory)
admin.site.register(Invitation)