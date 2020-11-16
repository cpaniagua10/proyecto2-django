from django.db import models
from django.conf import settings # default user model django

# Create your models here.

MOVIES = [
        ('1', 'Black Panther'),
        ('2', 'Moonlight'),
        ('3', 'Aladdin')]

TIME = [
    ('13:00', '13:00'),
    ('18:00', '18:00'),
]

class Seat(models.Model):
    number = models.CharField(max_length=2, blank = True, null = True)
    movie = models.CharField(max_length=9, choices=MOVIES)
    time = models.CharField(max_length=10,choices=TIME,blank = True, null = True)
    full = models.BooleanField(default=False)

    chosen_movie = models.CharField(max_length=150, blank = True, null = True)
    def __str__(self):
        if (self.movie == '1'):
            self.chosen_movie = 'Black Panther'
        elif (self.movie == '2'):
            self.chosen_movie = 'Moonlight'
        else:
            self.chosen_movie = 'Aladdin'
            
        return "Seat number: {} for movie {}. Time: {}".format(self.number,self.chosen_movie,self.time)

class Ticket(models.Model): 
        
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank = True, null = True)
    id = models.AutoField(primary_key=True) 
    movie = models.CharField(max_length=9, choices=MOVIES)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE, blank = True, null = True)


    def __str__(self):
        return "Ticket number: {}. Owner: {}".format(self.id,self.user)


