from django.db import models

from django.contrib.auth.models import AbstractUser
# Create your models here.
from django.utils.text import slugify
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
class BookingHistory(models.Model):
    roomID = models.CharField(max_length=10)
    location = models.CharField(max_length=10, default='LTK')  # LTK or other location
    slug = models.SlugField(
        verbose_name="Friendly URL",
        help_text="URL-friendly version of the booking info.",
        unique=True,
        blank=True  # allow it to be blank until auto-generated
    )
    date = models.DateTimeField(auto_now_add=True)
    date_booking = models.DateTimeField(default = '2025-01-01')
    # Many-to-Many relationship: one booking can involve multiple users, and each user can have multiple bookings.
    person = models.ManyToManyField(Users, related_name='book')
    
    # Example choices for time slot
    TIME_SLOT_CHOICES = [
        ('08:00–09:00', '08:00–09:00'),
        ('09:00–10:00', '09:00–10:00'),
        ('10:00–11:00', '10:00–11:00'),
        ('11:00–12:00', '11:00–12:00'),
        ('12:00–13:00', '12:00–13:00'),
        ('13:00–14:00', '13:00–14:00'),
        ('14:00–15:00', '14:00–15:00'),
        ('15:00–16:00', '15:00–16:00'),
        ('16:00–17:00', '16:00–17:00'),
        ('17:00–18:00', '17:00–18:00'),
        ('18:00–19:00', '18:00–19:00'),
    ]
    time_slot = models.CharField(max_length=20, choices=TIME_SLOT_CHOICES,default='08:00–09:00')
    is_cancelled = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.roomID} | {self.time_slot} | {self.date.date()}"
    
    def save(self, *args, **kwargs):
        # Auto-generate slug if it's not provided
        if not self.slug:
            # A simple auto-generation using slugify; customize as needed
            self.slug = slugify(f"{self.roomID}-{self.date}-{self.time_slot}")
        super().save(*args, **kwargs)

# Model for handling invitations related to a booking
class Invitation(models.Model):
    booking = models.ForeignKey(BookingHistory, on_delete=models.CASCADE, related_name='invitations')
    inviter = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='sent_invitations')
    invitee_email = models.EmailField(default='NG')
    invitee_username = models.CharField(max_length=20, default='NG')
    status = models.CharField(max_length=20, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Invitation to {self.invitee_email} - {self.status}"