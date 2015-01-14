from django.http import HttpResponse
from django.db import models
from hotels.models import Hotel, Room, Calendar

calendar = Calendar.objects.get(pk=2)
calendar.calendar_data = {
    2015-01-01: {available: 2,
                   bind: 0,
                   info: first,
                   notes: ,
                   price: 101,
                   promo: ,
                   status: available},
    2015-01-05: {available: 0,
                   bind: 0,
                   info: birthday,
                   notes: ,
                   price: 110,
                   promo: ,
                   status: booked}
}
