#from librarianAdmin.models import Room, Message as Message

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify
from django.conf import settings

class Room(models.Model):
    number = models.IntegerField(unique=True)
    name   = models.CharField(max_length=100)
    users = models.ManyToManyField(settings.AUTH_USER_MODEL)
    def __str__(self):
        return f"Room {self.number} - {self.name}"

class Message(models.Model):
    room      = models.ForeignKey(Room,
                                  on_delete=models.CASCADE)
    user      = models.ForeignKey(
                    settings.AUTH_USER_MODEL,
                    on_delete=models.SET_NULL,
                    null=True,
                    blank=True
                )
    content   = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        user_repr = self.user.username if self.user else 'Guest'
        return f"Message in Room {self.room.number} by {user_repr} at {self.timestamp}"