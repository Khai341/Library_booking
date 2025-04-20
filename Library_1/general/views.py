from django.shortcuts import render, redirect
import os
from django.http import JsonResponse
from librarianAdmin.models import BookingHistory
from django.utils import timezone
# Create your views here.
def ReturnMain(request):
    return render(request, 'general_main.html')

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
            return redirect('/libadmin/booking-history/')
    return render(request, 'general_booking.html')
    
    
    
def Ajax0 (request):
    #return render(request, 'main.html')
    user_input = request.POST.get("userInput", "")
    if user_input == "CS1":
        return render(request, 'map1.html')
    if user_input == "CS2":
        return render(request, 'map2.html')
    return #need a fallback
    
def Ajax1 (request):
    return JsonResponse({"message": f"056"}) 
    
def Ajax2 (request):
    return JsonResponse({"message": f"056"})
    
def save_new_booking(request, Location, Date, Room, Time):
    return render(request, 'general_booking.html')