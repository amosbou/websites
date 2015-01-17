from django.shortcuts import render
# from django.template import RequestContext, loader

# Create your views here.
from django.http import HttpResponse
from hotels.models import Hotel, Room, Calendar


def index(request):
    # rooms_list = Room.objects.order_by('room_name')

    context = {}
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


def three_rooms_list(request):
    rooms_list = Room.objects.order_by('room_name')

    context = {'rooms_list': rooms_list}
    return render(request, 'hotels/three-rooms-list.html', context)


def two_columns_rooms_list(request):
    rooms_list = Room.objects.order_by('room_name')

    context = {'rooms_list': rooms_list}
    return render(request, 'hotels/two-columns-rooms-list.html', context)


def room_with_one_bedroom(request, room_id):
    room = Room.objects.get(pk=room_id)
    context = {'room': room}
    return render(request, 'hotels/room-with-one-bedroom.html', context)


def reservation_page_2_2(request, room_id):
    room = Room.objects.get(pk=room_id)
    context = {'room': room}
    return render(request, 'hotels/reservation-page-2-2.html', context)






