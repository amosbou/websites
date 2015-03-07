from django.shortcuts import render
# from django.template import RequestContext, loader

# Create your views here.
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

from datetime import date, datetime, timedelta
from hotels.models import Hotel, Room, Booking
from django.db.models import Q

import datetime, logging
import subprocess
import paypalrestsdk
import json


def index_all_rooms(request):
    return index(request, 'yes')


def index(request, show_all_rooms='no'):
    if show_all_rooms == 'no':
        # show first 3 rooms
        rooms_list = Room.objects.order_by('name')[:1]
        booking_list = {}
        for room in rooms_list:
            booking_list[str(room.id)] = get_booking_list(room)
    else:
        # show all rooms
        rooms_list = Room.objects.order_by('name')
        booking_list = get_booking_list_all()
        print(booking_list)
    context = {'rooms_list': rooms_list, 'booking_list': booking_list}
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


def get_booking_list(room):
        booking_list_per_room = {}

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


def choose_room_page(request, room_id="-1"):
    context = {}
    print(" room_id " + room_id)
    check_in = False
    check_out = False
    check_out = False
    adults = False
    children = False
    if 'check-in' in request.POST and request.POST['check-in']:
        check_in = request.POST['check-in']
        context['check_in'] = check_in
    if 'check-out' in request.POST and request.POST['check-out']:
        check_out = request.POST['check-out']
        context['check_out'] = check_out
    if 'adults' in request.POST and request.POST['adults']:
        adults = request.POST['adults']
        context['adults'] = adults
    if 'children' in request.POST and request.POST['children']:
        children = request.POST['children']
        context['children'] = children

    if room_id == "-1":
        # no room selected yet. Look for available rooms
        print('check_in: ' + check_in + ' check_out: ' + check_out)
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

        # loop through the room to find all the rrom that are available in the selected user dates
        available_rooms = []
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
            # add the room to the list of available rooms
            available_rooms.append(room)

        context['available_rooms'] = available_rooms



        return render(request, 'hotels/reservation-page-choose-room.html', context)
    #    return HttpResponseRedirect(reverse('reservation_page', args=-1))
    room = Room.objects.get(pk=room_id)
    print("room " + room.__str__() + " room_id " + room_id)


    context['room'] = room
    # if check_in and check_out:
    #     return render(request, 'hotels/reservation-page-choose-room.html', context)

    return render(request, 'hotels/reservation-page-choose-date.html', context)


def checkout(request, room_id):
    room = Room.objects.get(pk=room_id)
    context = {}
    print(" room_id " + room_id)

    if 'check-in' in request.POST and request.POST['check-in']:
        context['check_in'] = request.POST['check-in']
    if 'check-out' in request.POST and request.POST['check-out']:
        context['check_out'] =request.POST['check-out']
    if 'adults' in request.POST and request.POST['adults']:
        context['adults'] = request.POST['adults']
    if 'children' in request.POST and request.POST['children']:
        context['children'] = request.POST['children']
    context['room'] = room
    return render(request, 'hotels/reservation-page-checkout.html', context)


def payment(request):
    context = {}
    method = False
    if 'method' in request.POST and request.POST['method']:
        context['method'] = request.POST['method']
        print(" method " + context['method'])
    if method and method == "credit card":
        return payment_card(request)
    return payment_paypal(request)


def payment_paypal(request):
    context = {}
    if 'resform-email' in request.POST and request.POST['resform-email']:
        context['resform-email'] = request.POST['resform-email']
        print(" email " + context['resform-email'])



    # Include Headers and Content by setting logging level to DEBUG, particularly for
    # Paypal-Debug-Id if requesting PayPal Merchant Technical Services for support
    logging.basicConfig(level=logging.INFO)

    api = paypalrestsdk.configure({"mode": "sandbox",  # sandbox or live
                                    "client_id":
                                    "AXsSKh46-KUXE9XV63prViA5XAU3bau92EjMB5QAD2GU0-sFDTugk2pU9nrcXvTfI-Jdw8FoWN8DuV5e",
                                    "client_secret":
                                    "EEsjnSGekYDHtCAHGRBSrQMlou0l33seg-XN8G7s7ehWqq2EqEDUXCi970Ba9Cf1dpfyyOY-1J6nv-UY"})
    # print(api.get_scope())
    print(api.get_access_token())

    # Payment
    # A Payment Resource; create one using
    # the above types and intent as 'sale'
    payment = paypalrestsdk.Payment({"intent": "sale",
                                    "redirect_urls": {
                                        "return_url": "http://127.0.0.1:8000/hotels/2/confirmation/",
                                        "cancel_url": "http://localhost:8000/hotels/2/checkout/"
                                    },
        "payer": {
            "payment_method": "paypal",
            "payer_info": {
                "tax_id_type": "BR_CPF",
                "tax_id": "Fh618775690"
            }
            },
        "transactions": [
            {
                "amount": {
                    "total": "34.07",
                    "currency": "USD",
                    "details": {
                        "subtotal": "30.00",
                        "tax": "0.07",
                        "shipping": "1.00",
                        "handling_fee": "1.00",
                        "shipping_discount": "1.00",
                        "insurance": "1.00"
                    }
                },
                "description": "This is the payment transaction description.",
                "custom": "EBAY_EMS_90048630024435",
                "invoice_number": "48787589677",
                "payment_options": {
                    "allowed_payment_method": "INSTANT_FUNDING_SOURCE"
                },
                "soft_descriptor": "ECHI5786786",
                "item_list": {
                    "items": [
                        {
                            "name": "bowling",
                            "description": "Bowling Team Shirt",
                            "quantity": "5",
                            "price": "3",
                            "tax": "0.01",
                            "sku": "1",
                            "currency": "USD"
                        },
                        {
                            "name": "mesh",
                            "description": "80s Mesh Sleeveless Shirt",
                            "quantity": "1",
                            "price": "17",
                            "tax": "0.02",
                            "sku": "product34",
                            "currency": "USD"
                        },
                        {
                            "name": "discount",
                            "quantity": "1",
                            "price": "-2.00",
                            "sku": "product",
                            "currency": "USD"
                        }
                    ],
                    "shipping_address": {
                        "recipient_name": "Betsy Buyer",
                        "line1": "111 First Street",
                        "city": "Saratoga",
                        "country_code": "US",
                        "postal_code": "95070",
                        "state": "CA"
                    }
                }
            }
            ]
    })

    # Create Payment and return status
    if payment.create():
        print("Payment[%s] created successfully" % payment.id)
        # Redirect the user to given approval url
        for link in payment.links:
            if link.method == "REDIRECT":
                # Convert to str to avoid google appengine unicode issue
                # https://github.com/paypal/rest-api-sdk-python/pull/58
                redirect_url = str(link.href)
                print("Redirect for approval: %s" % redirect_url)
                return HttpResponseRedirect(redirect_url)
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


def confirmation(request,room_id):
    context = {}
    return render(request, 'hotels/reservation-page-confirmation.html', context)