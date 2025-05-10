from django.contrib import admin
from .models import Room, RoomOccupation, Student

# Register your models here.
admin.site.register(Room)
admin.site.register(RoomOccupation)
admin.site.register(Student)
