from django.shortcuts import render, redirect
import os
from django.http import JsonResponse
from librarianAdmin.models import BookingHistory
from django.utils import timezone
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def ReturnMain(request):
    return render(request, 'general_main.html')

@login_required
def Booking(request):
    if request.method == 'POST':
        Location_booking = request.POST.get('Location_booking')
        Room_ID_booking = request.POST.get('Room_ID_booking')
        Date_booking = request.POST.get('Date_booking')
        Time_slot_booking = request.POST.get('Time_slot_booking')
        if Location_booking and Room_ID_booking and Date_booking and Time_slot_booking:
            booking_history = BookingHistory.objects.create(
            roomID=Room_ID_booking,
            location=Location_booking,
            date_booking=Date_booking,
            time_slot=Time_slot_booking,
            #person = request.user
            slug=f"{Room_ID_booking}-{'08:00–09:00'}-{timezone.now().strftime('%Y%m%d%H%M%S')}"
            )
            booking_history.person.add(request.user)
            return redirect('/book/booking-history/')
    return render(request, 'general_booking.html')
    
    
@login_required    
def Ajax0 (request):
    #return render(request, 'main.html')
    user_input = request.POST.get("userInput", "")
    if user_input == "CS1":
        return render(request, 'map1.html')
    if user_input == "CS2":
        return render(request, 'map2.html')
    return #need a fallback
@login_required   
def Ajax1 (request):
    user_booking = request.POST.get("user_booking", "")
    user_date = request.POST.get("user_date", "")
    booking = BookingHistory.objects.filter(date_booking=user_date,is_cancelled=False,roomID=user_booking)
    my_str = ""
    for book in booking:
        my_str += book.time_slot
        my_str += "|"
    return JsonResponse({"message": my_str}) 
    #return JsonResponse({"message": "08:00–09:00|09:00–10:00"}) 
@login_required    
def Ajax2 (request):
    return JsonResponse({"message": f"08:00–09:00"})
@login_required    
def save_new_booking(request, Location, Date, Room, Time):
    return render(request, 'general_booking.html')