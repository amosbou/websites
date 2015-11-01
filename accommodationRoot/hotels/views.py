from django.shortcuts import render
# from django.template import RequestContext, loader

# Create your views here.
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

# from datetime import date, datetime, timedelta
from hotels.models import Hotel, Room, Guest, Setting, RoomImage, ImageLayer
from django.db.models import Q

import pickle

from datetime import datetime, timedelta, date
# import subprocess
import paypalrestsdk
# import json
from hotels.room_data import start_rate
from hotels.room_data import get_nights_rates_in_season_for_num_of_guests


def index_all_rooms(request):
    return index(request, 'yes')


def index(request, show_all_rooms='no'):
    room_image_layers_dict = {}
    if show_all_rooms == 'no':
        # show first 3 rooms
        rooms_list = Room.objects.order_by('name')[:2]
        booking_list = {}
        overview_image_dict = {}
        for room in rooms_list:
            booking_list[str(room.id)] = get_booking_list(room)
            overview_image_dict[str(room.id)] = get_overview_image_dict(room)
            room_images_set = RoomImage.objects.filter(room__pk=room.pk)

            for room_image in room_images_set:
                image_layer_set = ImageLayer.objects.filter(room_image__pk=room_image.pk)
                room_image_layers_dict[room_image] = image_layer_set

    else:
        # show all rooms
        rooms_list = Room.objects.order_by('name')
        booking_list = get_booking_list_all()
        overview_image_dict = get_overview_image_dict_all()
    print(booking_list)
    print(overview_image_dict)
    print(overview_image_dict.keys())

    context = {'rooms_list': rooms_list, 'booking_list': booking_list, 'overview_image_dict': overview_image_dict,
               'room_image_layers_dict': room_image_layers_dict}
    return render(request, 'hotels/index.html', context)


# def accommodation(request, hotel_id):
#     hotels_list = Hotel.objects.order_by('city')
#     try:
#         hotel = Hotel.objects.get(pk=hotel_id)
#     except Hotel.DoesNotExist:
#         raise Http404
#     # rooms_list = hotel.room_set.all()
#     context = {'hotels_list': hotels_list, 'hotel': hotel}
#
#     return render(request, 'hotels/accommodation.html', context)
#

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


def get_booking_list_all():
    rooms_list = Room.objects.order_by('name')
    booking_list = {}

    for room in rooms_list:
        booking_list[str(room.id)] = get_booking_list(room)
    return booking_list


def get_image_dict_all():
    rooms_list = Room.objects.order_by('name')
    image_dict = {}

    for room in rooms_list:
        image_dict[str(room.id)] = get_image_dict(room)
    return image_dict


def get_image_dict(room):
    image_dict_per_room = {}
    room_image_set = room.roomimage_set.filter(room_id=room.id)
    for roomImage in room_image_set:
        if roomImage.purpose in image_dict_per_room:
            pass
        else:
            image_dict_per_room[roomImage.purpose] = []

        image_dict_per_room[roomImage.purpose].append(roomImage)
        print image_dict_per_room
    return image_dict_per_room


def get_overview_image_dict(room):
    image_dict_per_room = get_image_dict(room)
    if 'OVERVIEW' in image_dict_per_room:
        print('hello')
        return image_dict_per_room['OVERVIEW']
    else:
        return []


def get_overview_image_dict_all():
    rooms_list = Room.objects.order_by('name')
    overview_image_dict = {}

    for room in rooms_list:
        overview_image_dict[str(room.id)] = get_overview_image_dict(room)
    return overview_image_dict


def get_booking_list(room):
        booking_list_per_room = {}

        booking_set = room.booking_set.filter(check_out_date__gte=date.today())
        # booking_set = room.booking_set.filter(room_id=room.id)
        for booking in booking_set:
            booking_list_per_room[booking.check_in_date.strftime('%Y-%m-%d')] = {'available': '0',
                                                                                   'info': 'check_in',
                                                                                   'promo': '',
                                                                                   'bind': 1,
                                                                                   'notes': '',
                                                                                   'status': 'booked',
                                                                                   'price': room.base_rate}
            booking_list_per_room[booking.check_out_date.strftime('%Y-%m-%d')] = {'available': '0',
                                                                                    'info': 'check_out',
                                                                                    'promo': '',
                                                                                    'bind': 3,
                                                                                    'notes': '',
                                                                                    'status': 'booked',
                                                                                    'price': room.base_rate + 10}
            number_of_nights = booking.check_out_date - booking.check_in_date
            in_date = booking.check_in_date
            for i in range(number_of_nights.days - 1):
                in_date += timedelta(days=1)
                booking_list_per_room[in_date.strftime('%Y-%m-%d')] = {'available': '0',
                                                                                        'info': '',
                                                                                        'promo': '',
                                                                                        'bind': 2, 'notes': '',
                                                                                        'status': 'booked',
                                                                                        'price': room.base_rate + 20}

            print(booking.check_in_date)
            print(booking.check_out_date)
        return booking_list_per_room


def two_columns_rooms_list(request):
    rooms_list = Room.objects.order_by('name')
    booking_list = get_booking_list_all()
    print(booking_list)
    context = {'rooms_list': rooms_list, 'booking_list': booking_list}
    return render(request, 'hotels/two-columns-rooms-list.html', context)


def room_with_one_bedroom(request, room_id):
    room = Room.objects.get(pk=room_id)
    print(room)
    booking_list = get_booking_list(room)
    context = {'room': room, 'booking_list': booking_list}
    return render(request, 'hotels/room-with-one-bedroom.html', context)


def choose_date_page(request):
    context = {}
    return render(request, 'hotels/reservation-page-choose-date.html', context)


def get_formatted_date(date, dateformat='european'):
    print "date " + date
    if '-' in date:
        fields = date.split('-')
    else:
        fields = date.split('/')
    print fields
    formatted_date = fields[2] + '-' + fields[1] + '-' + fields[0]
    if dateformat == 'european':
        # format is dd-mm-yy
        formatted_date = fields[2] + '-' + fields[1] + '-' + fields[0]
    elif dateformat == 'american':
        # format received is mm/dd/yy
        formatted_date = fields[2] + '-' + fields[0] + '-' + fields[1]
    return formatted_date


def get_booking_data(request):
    context = {}
    check_in = ""
    check_out = ""
    children = '0'
    adults = '0'
    total_price = '0'
    first_name = ''
    last_name = ''
    email = ''
    if 'check-in' in request.POST and request.POST['check-in']:
        check_in = request.POST['check-in']
    if 'check-out' in request.POST and request.POST['check-out']:
        check_out = request.POST['check-out']
    if 'adults' in request.POST and request.POST['adults']:
        adults = request.POST['adults']
    if 'children' in request.POST and request.POST['children']:
        children = request.POST['children']
    if 'first_name' in request.POST and request.POST['first_name']:
        first_name = request.POST['first_name']
    if 'last_name' in request.POST and request.POST['last_name']:
        last_name = request.POST['last_name']
    if 'total_price' in request.POST and request.POST['total_price']:
        total_price = request.POST['total_price']
    if 'email' in request.POST and request.POST['email']:
        email = request.POST['email']
    context['check_in'] = check_in
    context['check_out'] = check_out
    try:
        context['adults'] = int(adults)
    except ValueError:
        context['adults'] = 2
    try:
        context['children'] = int(children)
    except ValueError:
        context['children'] = 0
    context['first_name'] = first_name
    context['last_name'] = last_name
    context['email'] = email
    context['total_price'] = float(total_price)
    return context


def choose_room_page(request, room_id="-1"):
    print 'choose_room_page'

    print(" room_id " + room_id)
    context = get_booking_data(request)
    check_in = context['check_in']
    check_out = context['check_out']

    setting = get_setting()
    date_format = setting.date_format

    check_in_date = get_formatted_date(check_in, date_format)
    check_out_date = get_formatted_date(check_out, date_format)
    adults = context['adults']
    children = context['children']

    available_rooms = []
    start_rates = {}
    nights_rates_breakdown = {}
    total_price_for_room = {}
    min_rate = {}
    if room_id == "-1":
        # no room selected yet. Look for available rooms
        print('check_in: ' + check_in + ' check_out: ' + check_out)
        print('dateformat ' + date_format + ' check_in_date: ' + check_in_date + ' check_out_date: ' + check_out_date)

        # loop through the room to find all the rooms that are available in the selected user dates
        for room in Room.objects.all():
            # if the requested user booking period overlaps/intersects with an existing booking period for a room,
            # that room is then unavailable
            booking_set = room.booking_set.filter((Q(check_out_date__gt=check_in_date)
                                                  & Q(check_out_date__lte=check_out_date))
                                                  | (Q(check_in_date__gte=check_in_date)
                                                     & Q(check_in_date__lt=check_out_date)))
            if booking_set.count() > 0:
                # there is an overlap/intersections with an existing booking period
                # the room with that booking is not available and therefore we skip it.
                continue
            # no intersection of the requested booking with any existing booking periods.
            # Therefore the room is available
            print('room ' + room.__str__())
            print '11111111111111111'
            # check that the number of adults is ok
            # booked_num_of_guests
            print('booked_num_of_guests = ' + str(adults) + ' ' + str(children))
            booked_num_of_guests = adults + children
            print('if ' + str(booked_num_of_guests) + ' > ' + str(room.max_num_of_guests) + ':')
            if booked_num_of_guests > room.max_num_of_guests:
                # booked num of guests is more than room capacity. we skip this room
                continue
                print '22222222222222'
            print '3333333333333333333333'
            # add the room to the list of available rooms
            available_rooms.append(room)
            context['available_rooms'] = available_rooms
            room_start_rate = start_rate(room.pk, check_in_date)
            start_rates[room.pk] = room_start_rate
            context['start_rates'] = start_rates
            check_in_date_object = datetime.strptime(check_in_date, "%Y-%m-%d").date()
            check_out_date_object = datetime.strptime(check_out_date, "%Y-%m-%d").date()
            nights_rates_breakdown_for_room = \
                get_nights_rates_in_season_for_num_of_guests(room.pk,
                                                             check_in_date_object,
                                                             check_out_date_object - timedelta(days=1),
                                                             adults + children
                                                             )
            nights_rates_breakdown[room.pk] = nights_rates_breakdown_for_room
            total_price_per_room = 0
            min_rate_per_room = 999999
            for day in nights_rates_breakdown_for_room:
                rate_per_day = nights_rates_breakdown_for_room[day]
                min_rate_per_room = min(min_rate_per_room, rate_per_day)
                total_price_per_room += rate_per_day
            if min_rate_per_room == 999999:
                min_rate_per_room = room.base_rate
            total_price_for_room[room.pk] = round(total_price_per_room * 100) / 100
            min_rate[room.pk] = min_rate_per_room
            print 'min_rate = ' + str(min_rate_per_room)
            print 'days_in_season 123' + str(nights_rates_breakdown_for_room)
        context['nights_rates_breakdown'] = nights_rates_breakdown
        context['total_price_for_room'] = total_price_for_room
        context['min_rate'] = min_rate
        return render(request, 'hotels/reservation-page-choose-room.html', context)
    #    return HttpResponseRedirect(reverse('reservation_page', args=-1))
    room = Room.objects.get(pk=room_id)
    print("room " + room.__str__() + " room_id " + room_id)
    available_rooms.append(room)
    context['available_rooms'] = available_rooms
    room_start_rate = start_rate(room.pk, check_in_date)
    start_rates[room.pk] = room_start_rate
    context['start_rates'] = start_rates
    check_in_date_object = datetime.strptime(check_in_date, "%Y-%m-%d").date()
    check_out_date_object = datetime.strptime(check_out_date, "%Y-%m-%d").date()
    nights_rates_breakdown_for_room = \
        get_nights_rates_in_season_for_num_of_guests(room.pk,
                                                     check_in_date_object,
                                                     check_out_date_object - timedelta(days=1),
                                                     adults + children
                                                     )
    print 'days_in_season xxx' + str(nights_rates_breakdown_for_room)
    nights_rates_breakdown[room.pk] = nights_rates_breakdown_for_room
    total_price_per_room = 0
    min_rate_per_room = 999999
    for day in nights_rates_breakdown_for_room:
        rate_per_day = nights_rates_breakdown_for_room[day]
        min_rate_per_room = min(min_rate_per_room, rate_per_day)
        total_price_per_room += rate_per_day
    if min_rate_per_room == 999999:
        min_rate_per_room = room.base_rate
    total_price_for_room[room.pk] = round(total_price_per_room * 100) / 100
    min_rate[room.pk] = min_rate_per_room
    print 'min_rate = ' + str(min_rate_per_room)
    print 'days_in_season 456' + str(nights_rates_breakdown_for_room)
    context['nights_rates_breakdown'] = nights_rates_breakdown
    context['total_price_for_room'] = total_price_for_room
    context['min_rate'] = min_rate
    return render(request, 'hotels/reservation-page-choose-room.html', context)


def checkout(request, room_id):
    room = Room.objects.get(pk=room_id)
    print('checkout room_id ' + room_id)
    print 'request.POST ' + str(request.POST)
    context = get_booking_data(request)
    check_in = context['check_in']
    check_out = context['check_out']
    adults = context['adults']
    children = context['children']
    setting = get_setting()
    date_format = setting.date_format

    check_in_date = get_formatted_date(check_in, date_format)
    check_out_date = get_formatted_date(check_out, date_format)

    context['room'] = room
    check_in_date_object = datetime.strptime(check_in_date, "%Y-%m-%d").date()
    check_out_date_object = datetime.strptime(check_out_date, "%Y-%m-%d").date()
    nights_rates_breakdown_for_room = \
        get_nights_rates_in_season_for_num_of_guests(room.pk,
                                                     check_in_date_object,
                                                     check_out_date_object - timedelta(days=1),
                                                     adults + children
                                                     )
    nights_rates_breakdown = {}
    total_price_for_room = {}
    nights_rates_breakdown[room.pk] = nights_rates_breakdown_for_room
    total_price_per_room = 0
    for day in nights_rates_breakdown_for_room:
        total_price_per_room += nights_rates_breakdown_for_room[day]

    print("total_price_per_room " + str(int(total_price_per_room)))
    total_price_for_room[room.pk] = "{0:.2f}".format(round(total_price_per_room * 100) / 100)
    dumps = pickle.dumps(total_price_for_room)
    request.session['total_price_for_room'] = dumps
    print 'Dumping: ', dumps
    context['total_price_for_room'] = total_price_for_room
    context['nights_rates_breakdown'] = nights_rates_breakdown
    return render(request, 'hotels/reservation-page-checkout.html', context)


def payment(request, room_id):

    print 'Payment request1 ' + str(request)
    if 'method' in request.POST and request.POST['method']:
        method = request.POST['method']
    if method and method == "credit card":
        return payment_card(request, room_id)
    return payment_paypal(request, room_id)


def payment_paypal(request, room_id):
    print 'Payment request2 ' + str(request)
    import logging
    room = Room.objects.get(pk=room_id)

    context = get_booking_data(request)
    print 'Context 1 ' + str(context)
    check_in = context['check_in']
    check_out = context['check_out']
    adults = int(context['adults'])
    children = int(context['children'])
    email = context['email']
    total_price = context['total_price']

    setting = get_setting()
    currency = setting.currency_code
    date_format = setting.date_format

    check_in_date = get_formatted_date(check_in, date_format)
    check_out_date = get_formatted_date(check_out, date_format)
    print 'check_in_date ' + check_in_date
    # Include Headers and Content by setting logging level to DEBUG, particularly for
    # Paypal-Debug-Id if requesting PayPal Merchant Technical Services for support
    logging.basicConfig(level=logging.INFO)

    # live data
    # api = paypalrestsdk.configure({"mode": "live",  # sandbox or live
    #                                 "client_id":
    #                                 "AQLGPsiNyr8-sGEIsdhmNZ7TkbcYOOJUgeZ-tZKvUoT-eZUDDzZFNNc0CKCMwAg57aFaQQFHLxsVRZff",
    #                                 "client_secret":
    #                                 "ELoMdz80tVSp-OyV8qRqtHq5qh0bntZahqVV3nMykA8FVrRbSfp8oZvTZCoyzACo9LWNPFp5JWYB91YQ"})
    # # Test - sandbox data
    api = paypalrestsdk.configure({"mode": "sandbox",  # sandbox or live
                                    "client_id":
                                    "AXsSKh46-KUXE9XV63prViA5XAU3bau92EjMB5QAD2GU0-sFDTugk2pU9nrcXvTfI-Jdw8FoWN8DuV5e",
                                    "client_secret":
                                    "EEsjnSGekYDHtCAHGRBSrQMlou0l33seg-XN8G7s7ehWqq2EqEDUXCi970Ba9Cf1dpfyyOY-1J6nv-UY"})
    # print(api.get_scope())
    print(api.get_access_token())
    print("Total: " + str(total_price))
    # Payment
    # A Payment Resource; create one using
    # the above types and intent as 'sale'
    payment = paypalrestsdk.Payment({"intent": "sale",
                                    "redirect_urls": {
                                        "return_url": "http://192.168.1.232:8000" + reverse('hotels:confirmation', args=(room_id,)),
                                        "cancel_url": "http://192.168.1.232:8000/hotels/2/checkout/"
                                    },
        "payer": {
            "payment_method": "paypal",
            },
        "transactions": [
            {
                "amount": {
                    "total": "{0:.2f}".format(total_price),
                    "currency": currency,

                },
                "description": room.hotel.name + " - " + room.name + ": check-in:" + check_in + " check-out:"
                                                                                              + check_out,
                "custom": room.hotel.name,
                "invoice_number": "48787589677",
                "payment_options": {
                    "allowed_payment_method": "INSTANT_FUNDING_SOURCE"
                },
                "soft_descriptor": "ECHI5786786",
                "item_list": {
                    "items": [
                        {
                            "name": room.hotel.name + "-" + room.name,
                            "description": room.description_short,
                            "quantity": "1",
                            "price": "{0:.2f}".format(total_price),
                            "sku": "1",
                            "currency": currency
                        }

                    ]

                }
            }
            ]
    })

    # Create Payment and return status
    if payment.create():
        print("Payment[%s] created successfully" % payment.id)
        # create the guest if it does not exist
        guest_data = {}
        guest_data['first_name'] = context['first_name']
        guest_data['last_name'] = context['last_name']
        guest_data['email_address'] = context['email']
        guest = get_create_guest(guest_data)
        request.session["context"] = context
        request.session["first_name"] = context['first_name']
        request.session["last_name"] = context['last_name']
        request.session["check_in"] = context['check_in']
        request.session["check_out"] = context['check_out']
        request.session["adults"] = context['adults']
        request.session["children"] = context['children']
        request.session["total_price"] = context['total_price']
        print '1. guest ' + str(guest_data)
        print '# Redirect the user to given approval url'
        # return HttpResponseRedirect(redirect_url, request, context)  #test

        for link in payment.links:
            if link.method == "REDIRECT":
                print ('Convert to str to avoid google appengine unicode issue')

                # redirect_url = str(link.href).replace(".paypal", ".sandbox.paypal")
                redirect_url = str(link.href)
                print("Redirect for approval: %s" % redirect_url)

                return HttpResponseRedirect(redirect_url, request)  # live

               #  return render(request, 'hotels/reservation-page-confirmation.html', context) #sandbox
    else:
        print("Error while creating payment:")
        print(payment.error)


def payment_card(request):
    context = {}
    # CreatePayment using credit card Sample
    # This sample code demonstrate how you can process
    # a payment with a credit card.
    # API used: /v1/payments/payment
    from paypalrestsdk import Payment
    import logging

    logging.basicConfig(level=logging.INFO)

    # Payment
    # A Payment Resource; create one using
    # the above types and intent as 'sale'

    api = paypalrestsdk.configure({"mode": "sandbox",  # sandbox or live
                                    "client_id":
                                    "AXsSKh46-KUXE9XV63prViA5XAU3bau92EjMB5QAD2GU0-sFDTugk2pU9nrcXvTfI-Jdw8FoWN8DuV5e",
                                    "client_secret":
                                    "EEsjnSGekYDHtCAHGRBSrQMlou0l33seg-XN8G7s7ehWqq2EqEDUXCi970Ba9Cf1dpfyyOY-1J6nv-UY"})

    print(api.get_access_token())

    # Payment
    # A Payment Resource; create one using
    # the above types and intent as 'sale'
    payment = paypalrestsdk.Payment({
                                    "intent": "sale",

                                    # Payer
                                    # A resource representing a Payer that funds a payment
                                    # Use the List of `FundingInstrument` and the Payment Method
                                    # as 'credit_card'
                                    "payer": {
                                        "payment_method": "credit_card",

                                        # FundingInstrument
                                        # A resource representing a Payeer's funding instrument.
                                        # Use a Payer ID (A unique identifier of the payer generated
                                        # and provided by the facilitator. This is required when
                                        # creating or using a tokenized funding instrument)
                                        # and the `CreditCardDetails`
                                        "funding_instruments": [{

                                            # CreditCard
                                            # A resource representing a credit card that can be
                                            # used to fund a payment.
                                            "credit_card": {
                                                "type": "visa",
                                                "number": "4417119669820331",
                                                "expire_month": "11",
                                                "expire_year": "2018",
                                                "cvv2": "874",
                                                "first_name": "Joe",
                                                "last_name": "Shopper",

                                                # Address
                                                # Base Address used as shipping or billing
                                                # address in a payment. [Optional]
                                                "billing_address": {
                                                    "line1": "52 N Main ST",
                                                    "city": "Johnstown",
                                                    "state": "OH",
                                                    "postal_code": "43210",
                                                    "country_code": "US"}}}]},
                                    # Transaction
                                    # A transaction defines the contract of a
                                    # payment - what is the payment for and who
                                    # is fulfilling it.
                                    "transactions": [{

                                        # ItemList
                                        "item_list": {
                                            "items": [{
                                                "name": "item",
                                                "sku": "item",
                                                "price": "1.00",
                                                "currency": "USD",
                                                "quantity": 1}]},

                                        # Amount
                                        # Let's you specify a payment amount.
                                        "amount": {
                                            "total": "1.00",
                                            "currency": "USD"},
                                        "description": "This is the payment transaction description."}]})

    # Create Payment and return status( True or False )
    if payment.create():
        print("Payment[%s] created successfully" % payment.id)
        return render(request, 'hotels/reservation-page-confirmation.html', context)
    else:
        # Display Error message
        print("Error while creating payment:")
        print(payment.error)


def get_setting():
    setting = Setting.objects.all()[0]
    return setting


def get_create_guest(guest_data):
    first_name = guest_data['first_name']
    last_name = guest_data['last_name']
    email = guest_data['email_address']
    guest_set = Guest.objects.filter(first_name=first_name, last_name=last_name, email_address=email)
    if guest_set:
        return guest_set[0]
    guest = Guest(first_name=first_name, last_name=last_name, email_address=email)
    guest.save()
    return guest


def confirmation(request, room_id):
    room = Room.objects.get(pk=room_id)
    context = {}
    context["first_name"] = "amos"
    context['last_name'] = request.session['last_name']
    context['check_in'] = request.session['check_in']
    context['check_out'] = request.session['check_out']
    context['adults'] = request.session['adults']
    context['children'] = request.session['children']
    context['total_price'] = request.session['total_price']

    print 'context xxx ' + str(context)
    setting = get_setting()
    date_format = setting.date_format
    context['date_format'] = date_format
    print 'Setting ' + str(setting)
    print ("this is the confirmation view")
    print 'name is ' + str(request.session['first_name'])
    print ('data_format ' + str(date_format))
    check_in = context['check_in']
    print ('check_in ' + str(check_in))
    check_out = context['check_out']
    adults = context['adults']
    children = context['children']

    check_in_date = get_formatted_date(check_in, date_format)
    check_out_date = get_formatted_date(check_out, date_format)

    check_in_date_object = datetime.strptime(check_in_date, "%Y-%m-%d").date()
    check_out_date_object = datetime.strptime(check_out_date, "%Y-%m-%d").date()
    nights_rates_breakdown ={}
    nights_rates_breakdown_for_room = \
        get_nights_rates_in_season_for_num_of_guests(room.pk,
                                                     check_in_date_object,
                                                     check_out_date_object - timedelta(days=1),
                                                     adults + children
                                                     )
    nights_rates_breakdown[room.pk] = nights_rates_breakdown_for_room
    context['nights_rates_breakdown'] = nights_rates_breakdown
    context['room'] = room
    total_price_for_room = pickle.loads(request.session['total_price_for_room'])
    context['total_price_for_room'] = total_price_for_room
    return render(request, 'hotels/reservation-page-confirmation.html', context)
