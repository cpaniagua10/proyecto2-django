from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Ticket


#form personalizado, es una replica del UserCreationForm de Django con mas fields
#ver documentacion para cambiar fields

class CreateUserForm(UserCreationForm):
    class Meta: 
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class BookingForm(forms.ModelForm):
    
    class Meta:
        SEATS = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5')]
        
        model = Ticket
        fields = ['user','movie','movie_date','seat_number','time']
        widgets = {
        'movie_date': forms.DateInput(format=('%d-%m-%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        'seat_number': forms.Select(choices=SEATS),
        }

        labels = {
                'user': 'User',
                'movie': 'Movie',
                'movie_date': 'Movie_date',
                'seat_number': 'Seat_number',
                'time':'Time'}

        