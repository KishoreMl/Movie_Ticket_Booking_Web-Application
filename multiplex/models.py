from django.db import models

class Movie(models.Model):
    movieName = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    description = models.TextField()
    language = models.CharField(max_length=100)
    print = models.CharField(max_length=100)
    image=models.ImageField(upload_to='Images')
    coverpic =models.ImageField(upload_to='Images')
    runtime = models.CharField(max_length=100)
    releasedate = models.CharField(max_length=100)
    certification = models.CharField(max_length=100)
    likes = models.IntegerField()
    released = models.BooleanField()

class Cast(models.Model):
    movieName = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    image=models.ImageField(upload_to='Images/cast')

class Crew(models.Model):
    movieName = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    image=models.ImageField(upload_to='Images/cast')

class Theatre(models.Model):
    theatreName = models.CharField(max_length=100) 
    location = models.CharField(max_length=100) 
    time1 = models.CharField(max_length=20)
    time2 = models.CharField(max_length=20)
    time3 = models.CharField(max_length=20)
    time4 = models.CharField(max_length=20)
    time5 = models.CharField(max_length=20)


class TicketTemporary(models.Model):
    ticketId = models.CharField(max_length=100)
    movieName = models.CharField(max_length=100)
    theatreName = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    seats = models.TextField()
    totalTickets = models.IntegerField()
    confee = models.IntegerField()
    subtotal = models.IntegerField()
    total = models.IntegerField()
    
class Ticket(models.Model):
    ticketId = models.CharField(max_length=100)
    movieName = models.CharField(max_length=100)
    theatreName = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    seats = models.TextField()
    totalTickets = models.IntegerField()
    confee = models.IntegerField()
    subtotal = models.IntegerField()
    total = models.IntegerField()



class Kirthika(models.Model):
    rowId = models.CharField(max_length=10)
    Seat1 = models.CharField(max_length=10)
    Seat2 = models.CharField(max_length=10)
    Seat3 = models.CharField(max_length=10)
    Seat4 = models.CharField(max_length=10)
    Seat5 = models.CharField(max_length=10)
    Seat6 = models.CharField(max_length=10)
    Seat7 = models.CharField(max_length=10)
    Seat8 = models.CharField(max_length=10)
    Seat9 = models.CharField(max_length=10)
    Seat10 = models.CharField(max_length=10)
    Seat11 = models.CharField(max_length=10)
    Seat12 = models.CharField(max_length=10)
    Seat13 = models.CharField(max_length=10)
    Seat14 = models.CharField(max_length=10)
    Seat15 = models.CharField(max_length=10)
    Seat16 = models.CharField(max_length=10)
    Seat17 = models.CharField(max_length=10)
    Seat18 = models.CharField(max_length=10)
    Seat19 = models.CharField(max_length=10)
    Seat20 = models.CharField(max_length=10)


class User(models.Model):

    userId =  models.CharField(max_length=100)
    phno = models.CharField(max_length=100)
    name  = models.CharField(max_length=100)
    cardno = models.CharField(max_length=100)
    ticketId = models.CharField(max_length=100)


