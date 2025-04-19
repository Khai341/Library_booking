from django.db import models

from django.contrib.auth.models import AbstractUser
# Create your models here.

class Users (AbstractUser):
    STATUS_CHOICES = [ #https://vindevs.com/blog/how-to-use-django-field-choices-with-code-examples-p60/  https://youtu.be/bpLJqMiv7UI?si=pGcQPRY6w78blnp1
        ('G', 'General User'),
        ('L', 'Librarian'),
        ('A', 'Admin'),
    ]
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='G')
    
    #id_number = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    image = models.ImageField(upload_to='students/', null=True, blank=True)

    def __str__(self):
        return self.username
    # pass = admin
class BookingHistory (models.Model):
    roomID = models.CharField(max_length=10)
    location = models.CharField(max_length=10, default='LTK')#LTK / DA
    slug = models.SlugField()
    date = models.DateTimeField(auto_now_add=True)
    person = models.ManyToManyField(Users, related_name='book')
# Get a Users by id
#Users = Users.objects.get(id=1)
# Get all BookingHistory written by this Users
#writer_posts = Users.book.all()
#https://stackoverflow.com/questions/61566808/manytomany-relationship-between-two-models-in-django 
    def __str__ (self):
        return self.roomID