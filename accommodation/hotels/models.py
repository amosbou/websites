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
    room_description_short = models.CharField(max_length=200, default="room short description")
    room_description_long = models.CharField(max_length=1000, default="room long description")
    room_caption = models.CharField(max_length=200, default="room caption")
    room_type = models.CharField(max_length=200, default="room type")
    room_double_bed_size = models.CharField(max_length=200, default="Double")
    room_double_bed_num_of = models.IntegerField(default=1)
    room_single_bed_size = models.CharField(max_length=200, default="Single")
    room_single_bed_num_of = models.IntegerField(default=1)
    room_max_num_of_guests = models.IntegerField(default=2)
    room_rate = models.FloatField(default=100)



    def __str__(self):
        return self.room_name


class Calendar(models.Model):
    room = models.OneToOneField(Room, primary_key=True)
    calendar_name = models.CharField(max_length=200, default="calendar name")
    calendar_data = models.CharField(max_length=1000)

    def __str__(self):
        return self.calendar_name


