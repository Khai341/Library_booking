from django.db import models
from librarianAdmin.models import Users
# Create your models here.
class Student(models.Model):
    id_number = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    image = models.ImageField(upload_to='students/', null=True, blank=True)

    def __str__(self):
        return self.id_number

class Room(models.Model):
    OCCUPIED = 'occupied'
    UNOCCUPIED = 'unoccupied'
    
    STATUS_CHOICES = [
        (OCCUPIED, 'Occupied'),
        (UNOCCUPIED, 'Unoccupied'),
    ]

    id_number = models.CharField(max_length=100, unique=True)
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default=UNOCCUPIED,
    )
    image = models.ImageField(upload_to='rooms/', null=True, blank=True) 

    ###students = models.ManyToManyField(Student, through='RoomOccupation')

    def __str__(self):
        return f"Room {self.id_number} ({self.status})"

class RoomOccupation(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    users = models.ManyToManyField(Users)
    occupied_on = models.DateTimeField()
    time_slot = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.student.name} occupied room {self.room.id_number} on {self.occupied_on}"