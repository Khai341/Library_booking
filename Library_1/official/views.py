from django.shortcuts import render
from .models import Room, Student
from librarianAdmin.models import Users
# Create your views here.
def official_list(request):
    query_room = request.GET.get('q_room', '')
    query_student = request.GET.get('q_student', '')

    # Filter rooms based on the search query (case insensitive search)
    rooms = Room.objects.all()
    if query_room:
        rooms = Room.objects.filter(id_number__icontains=query_room)

    # Filter students based on the search query (case insensitive search)
    students = Users.objects.all()
    if query_student:
        students = Users.objects.filter(id_number__icontains=query_student)

    # Pass the rooms and query to the template
    return render(request, 'official/official_list.html',  {'rooms': rooms, 'query_room': query_room, 'students': students, 'query_student': query_student})
