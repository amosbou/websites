from django.shortcuts import render
# from django.template import RequestContext, loader

# Create your views here.
from django.http import HttpResponse
from hotels.models import Hotel, Room, Calendar


def index(request):
    hotels_list = Hotel.objects.order_by('hotel_city')

    context = {'hotels_list': hotels_list}
    return render(request, 'hotels/index.html', context)


def accommodation(request, hotel_id):
    hotels_list = Hotel.objects.order_by('hotel_city')
    try:
        hotel = Hotel.objects.get(pk=hotel_id)
    except Hotel.DoesNotExist:
        raise Http404
    # rooms_list = hotel.room_set.all()
    context = {'hotels_list': hotels_list, 'hotel': hotel}

    return render(request, 'hotels/accommodation.html', context)


def room_details(request, hotel_id, room_id):
    hotels_list = Hotel.objects.order_by('hotel_city')
    hotel = Hotel.objects.get(pk=hotel_id)
    try:
        room = Room.objects.get(pk=room_id)
    except Hotel.DoesNotExist:
        raise Http404
    context = {'hotels_list': hotels_list, 'hotel': hotel, 'room': room}
    return render(request, 'hotels/room-detail.html', context)


def reservation_form(request, hotel_id, room_id):
    hotels_list = Hotel.objects.order_by('hotel_city')
    hotel = Hotel.objects.get(pk=hotel_id)
    try:
        room = Room.objects.get(pk=room_id)
    except Hotel.DoesNotExist:
        raise Http404
    context = {'hotels_list': hotels_list, 'hotel': hotel, 'room': room}
    return render(request, 'hotels/reservation-form.html', context)





