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
        model = Ticket
        fields = ['user','movie','seat']

        labels = {
                'user': 'User',
                'movie': 'Movie',
                'seat_number': 'Seat_number'
                }


        