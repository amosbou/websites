from __future__ import unicode_literals
from django.utils import encoding
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
    code = models.CharField(max_length=10, unique=True)
    description_short = models.CharField(max_length=200, default="room short description")
    description_long = models.CharField(max_length=1000, default="room long description")
    caption = models.CharField(max_length=200, default="room caption")
    type = models.CharField(max_length=200, default="room type")
    double_bed_size = models.CharField(max_length=200, default="Double")
    double_bed_num_of = models.IntegerField(default=1)
    single_bed_size = models.CharField(max_length=200, default="Single")
    single_bed_num_of = models.IntegerField(default=1)
    max_num_of_guests = models.IntegerField(default=2)
    base_rate = models.FloatField(default=100)
    num_of_guests_for_base_rate = models.IntegerField(default=2)
    num_of_guests_increment_for_extra_rate = models.IntegerField(default=2)
    extra_rate_for_guests_increment = models.FloatField(default=0.)
    extra_rate_percentage_for_guests_increment = models.FloatField(default=0.)

    def __str__(self):
        return self.name


class RoomImage(models.Model):
    room = models.ForeignKey(Room)
    path = models.CharField(max_length=500)
    purpose = models.CharField(max_length=50)
    resolution = models.CharField(max_length=100)
    order = models.IntegerField(default=1)

    def __str__(self):
        return self.path


class ImageLayer(models.Model):
    room_image = models.ForeignKey(RoomImage)
    text = models.CharField(max_length=500)
    div_attributes = models.CharField(max_length=1000, default='')
    order = models.IntegerField(default=1)

    def __str__(self):
        return self.div_attributes


class Country(models.Model):
    iso_code = models.CharField(max_length=20)
    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name


class Guest(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    email_address = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=50, default='')

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Address(models.Model):
    address = models.CharField(max_length=254)
    city = models.CharField(max_length=254)
    zipcode = models.CharField(max_length=20)
    country = models.ForeignKey(Country)

    def __str__(self):
        return self.address + ' ' + self.city + '\n' + self.zipcode + ', ' + str(self.country)


class AddressType(models.Model):
    type = models.CharField(max_length=30)


class GuestAddress(models.Model):
    unique_together = ['guest', 'address']
    guest = models.ForeignKey(Guest)
    address = models.ForeignKey(Address)
    address_type = models.ForeignKey(AddressType)


class Booking(models.Model):
    guest = models.ForeignKey(Guest)
    room = models.ForeignKey(Room)
    check_in_date = models.DateField(verbose_name="Check In")
    check_out_date = models.DateField(verbose_name="Check Out")
    date_created = models.DateField(verbose_name="Booking Date", auto_now_add=True)
    time_created = models.DateField(verbose_name="Booking Time", auto_now_add=True)

    def __str__(self):
        return "Check in: " + self.check_in_date.strftime('%d/%m/%Y') + " Check out: " + \
               self.check_out_date.strftime('%d/%m/%Y')


class Season(models.Model):
    name = models.CharField(max_length=30)
    start_date = models.DateField()
    end_date = models.DateField()
    room_season = models.ManyToManyField(Room, through='RoomSeason', through_fields=('season', 'room'))

    def __str__(self):
        return self.name


class RoomSeason(models.Model):
    season = models.ForeignKey(Season)
    room = models.ForeignKey(Room)
    rate = models.FloatField(default=100)

    class Meta:
        unique_together = ['room', 'season']

    def __str__(self):
        return "Season: " + str(self.season) + ' for Room:' + str(self.room)


class Setting(models.Model):
    date_format = models.CharField(max_length=12, default="european")
    currency_symbol = models.CharField(max_length=12, default=u"\u00A3")
    currency_code = models.CharField(max_length=12, default="GBP")

    def __str__(self):

        return "Date Format: " + self.date_format + "\nCurrency: "\
               + encoding.smart_str(self.currency_symbol.encode('unicode-escape'), encoding='ascii', errors='ignore')



