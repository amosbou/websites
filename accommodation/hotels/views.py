from django.shortcuts import render
# from django.template import RequestContext, loader

# Create your views here.
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from datetime import date, datetime, timedelta
from hotels.models import Hotel, Room, Booking
from django.db.models import Q

import datetime, logging


def index(request):
    # rooms_list = Room.objects.order_by('room_name')

    context = {}
    return render(request, 'hotels/index.html', context)


def accommodation(request, hotel_id):
    hotels_list = Hotel.objects.order_by('city')
    try:
        hotel = Hotel.objects.get(pk=hotel_id)
    except Hotel.DoesNotExist:
        raise Http404
    # rooms_list = hotel.room_set.all()
    context = {'hotels_list': hotels_list, 'hotel': hotel}

    return render(request, 'hotels/accommodation.html', context)


def room_details(request, hotel_id, room_id):
    hotels_list = Hotel.objects.order_by('city')
    hotel = Hotel.objects.get(pk=hotel_id)
    try:
        room = Room.objects.get(pk=room_id)
    except Hotel.DoesNotExist:
        raise Http404
    context = {'hotels_list': hotels_list, 'hotel': hotel, 'room': room}
    return render(request, 'hotels/room-detail.html', context)


def three_rooms_list(request):
    rooms_list = Room.objects.order_by('name')

    context = {'rooms_list': rooms_list}
    return render(request, 'hotels/three-rooms-list.html', context)


def date_range_generator(start, end, delta):
    curr = start
    while curr < end:
        yield curr
        curr += delta


def two_columns_rooms_list(request):

    rooms_list = Room.objects.order_by('name')
    booking_list = {}

    for room in rooms_list:
        booking_list_per_room = {}
        # for available_date in date_range_generator(datetime.date.today(),
        #                                            datetime.date.today() + datetime.timedelta(days=365),
        #                                            timedelta(days=1)):
        #
        #     #  Day status (none, available, booked, special, unavailable)
        #     booking_list_per_room[available_date.strftime('%Y-%m-%d')] = {'available': '1',
        #                                                                   'info': 'Available to book',
        #                                                                   'promo': '',
        #                                                                   'bind': 0, 'notes': 'These are the notes',
        #                                                                   'status': 'available',
        #                                                                   'price': room.rate + 20}

        booking_set = room.booking_set.filter(check_out_date__gte=datetime.date.today())
        # booking_set = room.booking_set.filter(room_id=room.id)
        for booking in booking_set:
            booking_list_per_room[booking.check_in_date.strftime('%Y-%m-%d')] = {'available': '0',
                                                                                   'info': 'check_in',
                                                                                   'promo': '',
                                                                                   'bind': 1,
                                                                                   'notes': '',
                                                                                   'status': 'booked',
                                                                                   'price': room.rate}
            booking_list_per_room[booking.check_out_date.strftime('%Y-%m-%d')] = {'available': '0',
                                                                                    'info': 'check_out',
                                                                                    'promo': '',
                                                                                    'bind': 3,
                                                                                    'notes': '',
                                                                                    'status': 'booked',
                                                                                    'price': room.rate + 10}
            number_of_nights = booking.check_out_date - booking.check_in_date
            in_date = booking.check_in_date
            for i in range(number_of_nights.days - 1):
                in_date += datetime.timedelta(days=1)
                booking_list_per_room[in_date.strftime('%Y-%m-%d')] = {'available': '0',
                                                                                        'info': '',
                                                                                        'promo': '',
                                                                                        'bind': 2, 'notes': '',
                                                                                        'status': 'booked',
                                                                                        'price': room.rate + 20}

            print(booking.check_in_date)
            print(booking.check_out_date)

        booking_list[str(room.id)] = booking_list_per_room
        print(booking_list)
    context = {'rooms_list': rooms_list, 'booking_list': booking_list}
    return render(request, 'hotels/two-columns-rooms-list.html', context)


def room_with_one_bedroom(request, room_id):
    room = Room.objects.get(pk=room_id)
    context = {'room': room}
    return render(request, 'hotels/room-with-one-bedroom.html', context)


def choose_date_page(request):
    context = {}
    return render(request, 'hotels/reservation-page-choose-date.html', context)


def choose_room_page(request, room_id="-1"):
    context = {}
    print(" room_id " + room_id)
    check_in = False
    check_out = False
    if 'check-in' in request.POST and request.POST['check-in']:
        check_in = request.POST['check-in']
        context['check_in'] = check_in
    if 'check-out' in request.POST and request.POST['check-out']:
        check_out = request.POST['check-out']
        context['check_out'] = check_out

    if room_id == "-1":
        # no room selected yet. Look for available rooms
        print('check_out ' + check_out)
        dateformat = request.POST['dateformat']
        if dateformat == 'european':
            # format is dd-mm-yy
            fields = check_in.split('-')
            check_in_date = fields[2] + '-' + fields[1] + '-' + fields[0]
            fields = check_out.split('-')
            check_out_date = fields[2] + '-' + fields[1] + '-' + fields[0]
        elif dateformat == 'american':
            # format received is mm/dd/yy
            fields = check_in.split('-')
            check_in_date = fields[2] + '-' + fields[0] + '-' + fields[1]
            fields = check_out.split('-')
            check_out_date = fields[2] + '-' + fields[0] + '-' + fields[1]

        booking_set = Booking.objects.filter(Q(check_out_date__lte=check_in_date) | Q(check_in_date__gte=check_out_date))
        print(booking_set)
        rooms = []
        for booking in booking_set:
            room = booking.room
            rooms.append(room)
            print('room ' + room.__str__() + ' booking ' + booking.__str__())

        context['rooms'] = rooms



        return render(request, 'hotels/reservation-page-choose-room.html', context)
    #    return HttpResponseRedirect(reverse('reservation_page', args=-1))
    room = Room.objects.get(pk=room_id)
    print("room " + room.__str__() + " room_id " + room_id)


    context['room'] = room
    if check_in and check_out:
        return render(request, 'hotels/reservation-page-choose-room.html', context)

    return render(request, 'hotels/reservation-page-choose-date.html', context)




