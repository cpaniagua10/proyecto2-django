from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm, BookingForm
from .models import Seat, Ticket
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def home(request): 
	return render(request, 'main.html')
def registerPage(request): 
    form = CreateUserForm()
    if request.method == 'POST': 
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('loginPage')
    context = {'form':form}
    return render(request, 'register.html', context)

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None: 
            login(request, user)
            return redirect('home') #hay que cambiarlo por homepage pero no existe aun
        else: 
            messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, 'login.html', context)

def logoutUser(request): 
    logout(request)
    return redirect('loginPage')


def ticketBooking(request):
    new_form = BookingForm()
    seat_dict = {}
    for seat in Seat.objects.all():
        if (not seat.full):
            seat_dict[seat.pk] = {
                'number': seat.number,
                'movie': seat.movie,
                'time': seat.time,
            }

    if (request.method == 'POST'):
        filled_form = BookingForm(request.POST)

        if (filled_form.is_valid()):
            if (filled_form.cleaned_data.get('seat').full):
                note = 'That seat is not available, please choose another one'
            else:
                new_ticket = filled_form.save()
                seat_form = filled_form.cleaned_data.get('seat')
                Seat.objects.filter(pk=seat_form.pk).update(full=True)
                note = 'Your ticket has been created'

            seat_dict_filled = {}
            for seat in Seat.objects.all():
                if (not seat.full):
                    seat_dict_filled[seat.pk] = {
                        'number': seat.number,
                        'movie': seat.movie,
                        'time': seat.time,
                    }
        else:
            note = 'INVALID, try again.'

        return render(
            request,
            'booking.html',
            {
                'bookingform': new_form,
                'note': note,
                'seat_dict': seat_dict_filled
            }
        )
    else:

        return render(
            request,
            'booking.html',
            {
                'bookingform': new_form,
                'note': 'Choose your movie, time and seat:',
                'seat_dict': seat_dict,
            }
        )

def show(request): 
    if request.user.is_authenticated:
        ticket_dict = {}
        username = request.user.username
        print(username)
        for ticket in Ticket.objects.all():
            if str(ticket.user) == username or username == 'carolina':
                ticket_dict[ticket.pk] = {
                    'seat': ticket.seat,
                'user': ticket.user
                }   
        return render(
                request,
                'show.html',
                {
                    'ticket_dict': ticket_dict
                }
            )
    else:
        return redirect('loginPage')
