from django.shortcuts import render
# from django.template import RequestContext, loader

# Create your views here.
from django.http import HttpResponse
from hotels.models import Hotel, Room, Booking

import datetime, logging


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


def three_rooms_list(request):
    rooms_list = Room.objects.order_by('room_name')

    context = {'rooms_list': rooms_list}
    return render(request, 'hotels/three-rooms-list.html', context)


def two_columns_rooms_list(request):

    rooms_list = Room.objects.order_by('room_name')
    booking_list = {}

    for room in rooms_list:
        booking_set = room.booking_set.filter(booking_check_out_date__gte=datetime.date.today())
        # booking_set = room.booking_set.filter(room_id=room.id)
        booking_list_per_room = {}
        for booking in booking_set:
            booking_list_per_room[booking.booking_check_in_date.strftime('%Y-%m-%d')] = {'available': '0',
                                                                                   'info': 'check_in',
                                                                                   'promo': '',
                                                                                   'bind': 0,
                                                                                   'notes': '',
                                                                                   'status': 'available',
                                                                                   'price': room.room_rate}
            booking_list_per_room[booking.booking_check_out_date.strftime('%Y-%m-%d')] = {'available': '0',
                                                                                    'info': 'check_out',
                                                                                    'promo': '',
                                                                                    'bind': 0,
                                                                                    'notes': '',
                                                                                    'status': 'available',
                                                                                    'price': room.room_rate + 10}
            numberOfNights = booking.booking_check_out_date - booking.booking_check_in_date
            in_date = booking.booking_check_in_date
            for i in range(numberOfNights.days - 1):
                in_date += datetime.timedelta(days=1)
                booking_list_per_room[in_date.strftime('%Y-%m-%d')] = {'available': '0',
                                                                                        'info': '',
                                                                                        'promo': '',
                                                                                        'bind': 0, 'notes': '',
                                                                                        'status': 'available',
                                                                                        'price': room.room_rate + 20}

            print(booking.booking_check_in_date)
            print(booking.booking_check_out_date)

        booking_list[str(room.id)] = booking_list_per_room
        print(booking_list)
    context = {'rooms_list': rooms_list, 'booking_list': booking_list}
    return render(request, 'hotels/two-columns-rooms-list.html', context)


def room_with_one_bedroom(request, room_id):
    room = Room.objects.get(pk=room_id)
    context = {'room': room}
    return render(request, 'hotels/room-with-one-bedroom.html', context)


def reservation_page(request, room_id):

    room = Room.objects.get(pk=room_id)
    context = {}
    check_in = False
    check_out = False
    if 'check-in' in request.POST and request.POST['check-in']:
        check_in = request.POST['check-in']
        context['check_in'] = check_in
    if 'check-out' in request.POST and request.POST['check-out']:
        check_out = request.POST['check-out']
        context['check_out'] = check_out
    context['room'] = room
    if check_in and check_out:
        return render(request, 'hotels/reservation-page-choose-room.html', context)

    return render(request, 'hotels/reservation-page-choose-date.html', context)




