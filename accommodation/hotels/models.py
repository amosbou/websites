from django.db import models

# Create your models here.


class Hotel(models.Model):
    hotel_name = models.CharField(max_length=200)
    hotel_city = models.CharField(max_length=200)

    def __str__(self):
        return self.hotel_name


class Room(models.Model):
    hotel = models.ForeignKey(Hotel)
    room_name = models.CharField(max_length=200)
    room_type = models.CharField(max_length=200)

    def __str__(self):
        return self.room_name


