from django.db import models

# Create your models here.


class Hotel(models.Model):
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Room(models.Model):
    hotel = models.ForeignKey(Hotel)
    name = models.CharField(max_length=200)
    description_short = models.CharField(max_length=200, default="room short description")
    description_long = models.CharField(max_length=1000, default="room long description")
    caption = models.CharField(max_length=200, default="room caption")
    type = models.CharField(max_length=200, default="room type")
    double_bed_size = models.CharField(max_length=200, default="Double")
    double_bed_num_of = models.IntegerField(default=1)
    single_bed_size = models.CharField(max_length=200, default="Single")
    single_bed_num_of = models.IntegerField(default=1)
    max_num_of_guests = models.IntegerField(default=2)
    rate = models.FloatField(default=100)

    def __str__(self):
        return self.name


class Booking(models.Model):
    room = models.ForeignKey(Room)
    check_in_date = models.DateField(verbose_name="Check In")
    check_out_date = models.DateField(verbose_name="Check Out")
    date_created = models.DateField(verbose_name="Booking Date", auto_now_add=True)
    time_created = models.DateField(verbose_name="Booking Time", auto_now_add=True)

    def __str__(self):
        return "Check in: " + self.check_in_date.strftime('%d/%m/%Y') + " Check out: " + \
               self.check_out_date.strftime('%d/%m/%Y')


class Settings(models.Model):
    date_format = models.CharField(max_length=12, default="dd/mm/yy")
    currency = models.CharField(max_length=3, default=u"\u00A3")

    def __str__(self):
        return "Date Format: " + self.date_format\
               + "\nCurrency: " + self.currency


