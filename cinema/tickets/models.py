from django.db import models
from django.conf import settings # default user model django

# Create your models here.


class Ticket(models.Model): 
    MOVIES = [
        ('1', 'movie-one'),
        ('2', 'movie-two'),
        ('3', 'movie-three')]

    TIME = [
        ('1', '13:00'),
        ('2', '14:00'),
        ('3', '15:00')
    ]
        
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank = True, null = True)
    id = models.AutoField(primary_key=True) 
    movie = models.CharField(max_length=9, choices=MOVIES)
    movie_date = models.DateField(blank = True, null = True)
    seat_number = models.CharField(max_length=2, blank = True, null = True)
    time = models.CharField(max_length=10,choices=TIME,blank = True, null = True)

    def __str__(self):
        return "Ticket number: {}. Owner: {}".format(self.id,self.user)

# class BookingTickets(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
#     movie_date = models.CharField(max_length=150)