from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from .models import BookingHistory, Invitation
from django.utils import timezone

from django.http import HttpResponse
# Main page view
@login_required
def return_main(request):
    #return render(request, 'librarianAdmin_main.html')
    return render(request, 'general_main.html')

# Booking history view
@login_required
def booking_history(request):
  # Assuming the related_name in your BookingHistory model is 'book'
    # This will fetch all active (not cancelled) bookings for the current user
    bookings = request.user.book.filter(is_cancelled=False).order_by('-date')
    invitation = Invitation.objects.filter(invitee_username=request.user.username)
    # Render a template (you can choose the same or a different template)
    return render(request, 'booking/booking_history.html', {'bookings': bookings, 'invitation': invitation})

@login_required
def booking_detail(request, booking_id):
    # Show detailed information about a specific booking.
    booking = get_object_or_404(BookingHistory, id=booking_id)
    #return render(request, 'booking/booking_detail.html', {'booking': booking})
    if request.user in booking.person.all():
        return render(request, 'booking/booking_detail.html', {'booking': booking})
    else:
        return HttpResponse("Not found")

@login_required
def send_invitation(request, booking_id):
    # Allows user to send an invitation for a specific booking.
    booking = get_object_or_404(BookingHistory, id=booking_id)
    if request.method == "POST":
        invitee_email = None
        #invitee_email = request.POST.get('invitee_email')
        invitee_username = request.POST.get('invitee_username')
        # Create the invitation record
        Invitation.objects.create(
            booking=booking,
            inviter=request.user,
            invitee_username=invitee_username
        )
        #return redirect('booking_history')
        return redirect('/book/booking-history')
    return render(request, 'booking/send_invitation.html', {'booking': booking})

@login_required
def rebook(request, booking_id):
    booking = get_object_or_404(BookingHistory, id=booking_id)
    
    if request.method == "POST":
        new_booking = BookingHistory.objects.create(
            roomID=booking.roomID,
            location=booking.location,
            time_slot=booking.time_slot,
            slug=f"{booking.roomID}-{booking.time_slot}-{timezone.now().strftime('%Y%m%d%H%M%S')}"
        )
        new_booking.person.add(request.user)
        return redirect('librarianAdmin:booking_history')  # namespaced!
    
    return render(request, 'booking/rebook.html', {'booking': booking})

#@require_POST
@login_required
def cancel_booking(request, booking_id):
    booking = get_object_or_404(BookingHistory, id=booking_id)
    # Optional: Verify that the user is authorized to cancel this booking
    if request.user in booking.person.all():
        booking.is_cancelled = True
        booking.save()
    return redirect('/book/booking-history')


@login_required
def delete_invitation(request, datetime_str):
    # Allows user to send an invitation for a specific booking.
    invitation = Invitation.objects.filter(invitee_username=request.user.username,created_at=datetime_str)
    if invitation != None:   
        invitation.delete()
    return redirect('/book/booking-history')
    
    
    
@login_required
def accept_invitation(request, datetime_str):
    # Allows user to send an invitation for a specific booking.
    invitation = Invitation.objects.filter(invitee_username=request.user.username,created_at=datetime_str)
    if invitation != None:  
        invitation = invitation.first()
        my_book = invitation.booking
        my_book.person.add(request.user)
        invitation.delete()
    return redirect('/book/booking-history')