from django.db import models
from django.contrib.auth.models import User

class Pilot(models.Model):
    POSITION_CHOICES = [
        ("JN", "Junior"),
        ("SN", "Senior"),
        ("IM", "Intermediate"),
    ]
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    birth_date = models.DateField()
    flight_hours_total = models.IntegerField()
    position = models.CharField(max_length=100, choices=POSITION_CHOICES)

    def __str__(self):
        return self.name+" "+ self.surname

class AirBalloon(models.Model):
    BALLOON_TYPES = [
        ("S", "Small"),
        ("M", "Medium"),
        ("L", "Large"),
    ]
    type = models.CharField(max_length=1, choices=BALLOON_TYPES)
    manufacturer = models.CharField(max_length=100)
    max_capacity = models.IntegerField()

    def __str__(self):
        return self.manufacturer+" ("+self.type+")"

class Airline(models.Model):
    name = models.CharField(max_length=100)
    year_founded = models.IntegerField()
    flies_outside_Europe = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class AirlinePilot(models.Model):
    airline = models.ForeignKey(Airline, on_delete=models.CASCADE)
    pilot = models.ForeignKey(Pilot, on_delete=models.CASCADE)

    def __str__(self):
        return self.airline.name + " (" + self.pilot.name + ")"

class Flight(models.Model):
    code = models.CharField(max_length=100, blank=False)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)
    airline_pilot = models.ForeignKey(AirlinePilot, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="airbaloon/images/", blank=True)
    air_balloon = models.ForeignKey(AirBalloon, on_delete=models.CASCADE)
    departure_airport = models.CharField(max_length=100)
    arrival_airport = models.CharField(max_length=100)

    def __str__(self):
        return "Flight "+self.code + ", operated by " + str(self.airline_pilot)