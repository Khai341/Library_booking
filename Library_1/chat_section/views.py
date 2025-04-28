import random
from django.shortcuts import render, redirect, get_object_or_404
from .models import Room, Message
from librarianAdmin.models import Users
from .utils import get_online_room_numbers

from django.contrib.auth.decorators import login_required
def home(request):
    return render(request, 'chat_section/home.html')

def room_list(request):

    rooms = [
        {"title": "Invitation", "name": "Chat room 101", "time": "07/04/2025, 7h-8h"},
        {"title": "Available Chat", "name": "Chat room 001", "time": "07/04/2025, 7h-8h"},
    ]

    return render(request, 'chat_section/rooms.html', {'rooms': rooms})

def chat_rooms_redirect(request):
    random_number = random.randint(1, 50)
    return redirect('chat_rooms', number=random_number)

@login_required
def chat_rooms(request, number):
    all_rooms = Room.objects.filter(users=request.user).order_by('number')
    room = Room.objects.filter(users=request.user,number=number).first()
    message = None
    if room:
        message = Message.objects.filter(room=room)
    else:
        number = 0
    
    #online_rooms = get_online_room_numbers()
    online_rooms = Room.objects.all()
    return render(request, 'chat_section/chat_rooms.html', {
        'room': room,
        'user': request.user,
        'messages': message,
        'all_rooms': all_rooms,
        'current_number': number,
        'online_rooms': online_rooms,
    })



    """
    #room = get_object_or_404(Room, number=number)
    room = Room.objects.filter(number=number).first()
    message = None
    if room:
        message = Message.objects.filter(room=room)
    else:
        number = 0
    all_rooms = Room.objects.order_by('number')
    #online_rooms = get_online_room_numbers()
    online_rooms = Room.objects.all()
    return render(request, 'chat_section/chat_rooms.html', {
        'room': room,
        'user': request.user,
        'messages': message,
        'all_rooms': all_rooms,
        'current_number': number,
        'online_rooms': online_rooms,
    })
    """
