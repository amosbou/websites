__author__ = 'cloudexplorer'

from hotels.models import Room
from django.db.models import Q
from datetime import datetime, timedelta
import collections


def start_rate(room_id, start_date):
    print 'start_rate(' + str(room_id) + ' ' + str(start_date)
    room = Room.objects.get(pk=room_id)
    room_season_set = room.roomseason_set.filter(room=room)\
        .filter(season__start_date__lte=start_date)\
        .filter(season__end_date__gte=start_date)
    room_season_set
    if not room_season_set:
        return room.base_rate
    for room_season in room_season_set:
        return room_season.rate


def get_roomseason_set_in_dates(room_id, start_date, end_date):
    room = Room.objects.get(pk=room_id)
    # find seasons that fully contain the booking period
    # find seasons that are fully contained withing the booking period
    # find seasons that starts before or at check_in date but ends before or at check_out date
    # find seasons that starts at or after check_in date and ends at or after check_out date
    roomseason_set = room.roomseason_set.filter((Q(season__start_date__lte=start_date)
                                                 & Q(season__end_date__gte=end_date))
                                                | (Q(season__start_date__gte=start_date)
                                                    & Q(season__end_date__lte=end_date))
                                                | (Q(season__start_date__lte=start_date)
                                                    & Q(season__end_date__lte=end_date)
                                                    & Q(season__end_date__gte=start_date))
                                                | (Q(season__start_date__gte=start_date)
                                                    & Q(season__start_date__lte=end_date)
                                                    & Q(season__end_date__gte=end_date)))
    print 'unbelievable season ' + str(roomseason_set)
    return roomseason_set


def get_nights_rates_in_season(room_id, start_date, end_date):
    print('def days_in_season(' + str(room_id) + ',' + str(start_date) + ',' + str(end_date) + '):')
    season_days_range = {}
    roomseason_set = get_roomseason_set_in_dates(room_id, start_date, end_date)
    print 'roomseason_set ' + str(roomseason_set)
    if roomseason_set:
        print 'yyyyyyyyyes'
    else:
        print 'nnnnnnnoo'
    room = Room.objects.get(pk=room_id)
    timedelta_range = end_date - start_date + timedelta(days=1)
    in_season_date = start_date
    for i in range(timedelta_range.days):
        season_days_range[in_season_date] = room.base_rate
        print('in_season_date ' + str(in_season_date))
        in_season_date += timedelta(days=1)
    for roomseason in roomseason_set:
        date_range = {}
        if start_date > roomseason.season.start_date:
            date_range['start_date'] = start_date
        else:
            date_range['start_date'] = roomseason.season.start_date
        if end_date < roomseason.season.end_date:
            date_range['end_date'] = end_date
        else:
            date_range['end_date'] = roomseason.season.end_date
        timedelta_range = date_range['end_date'] - date_range['start_date'] + timedelta(days=1)
        in_season_date = date_range['start_date']
        for i in range(timedelta_range.days):
            season_days_range[in_season_date] = roomseason.rate
            print('in_season_date ' + str(in_season_date))
            in_season_date += timedelta(days=1)
    ordered_dates = season_days_range.keys()
    ordered_dates.sort()
    ordered_dates_rates = collections.OrderedDict()
    for date in ordered_dates:
        ordered_dates_rates[date.strftime("%A, %B %d, %Y")] = season_days_range[date]

    print('ordered_dates_rates ' + str(ordered_dates_rates))

    return ordered_dates_rates


def get_nights_rates_in_season_for_num_of_guests(room_id, start_date, end_date, num_of_guests):
    print 'hello '
    room = Room.objects.get(pk=room_id)
    num_of_guests_for_base_rate = room.num_of_guests_for_base_rate
    print 'num_of_guests_for_base_rate ' + str(num_of_guests_for_base_rate)
    num_of_guests_increment_for_extra_rate = room.num_of_guests_increment_for_extra_rate
    extra_rate_for_guests_increment = room.extra_rate_for_guests_increment
    extra_rate_percentage_for_guests_increment = room.extra_rate_percentage_for_guests_increment

    nights_rates_breakdown_for_room = get_nights_rates_in_season(room_id, start_date, end_date)
    adjusted_nights_rates_breakdown_for_room = collections.OrderedDict()
    for night in nights_rates_breakdown_for_room:
        print ' night ' + str(night)
        night_basic_rate = nights_rates_breakdown_for_room[night]
        print 'night_basic_rate ' + str(night_basic_rate)
        if num_of_guests <= num_of_guests_for_base_rate:
            adjusted_nights_rates_breakdown_for_room[night] = night_basic_rate
            continue
        extra_guests = num_of_guests - num_of_guests_for_base_rate
        print 'extra_guests ' + str(extra_guests)
        number_of_increments = round(0.25 + float(extra_guests) / num_of_guests_increment_for_extra_rate)
        print 'number_of_increments ' + str(number_of_increments)
        if extra_rate_for_guests_increment > 0.:
            adjusted_nights_rates_breakdown_for_room[night] = night_basic_rate +\
                number_of_increments * extra_rate_for_guests_increment
        else:
            adjusted_nights_rates_breakdown_for_room[night] = night_basic_rate *\
                (1 + number_of_increments * extra_rate_percentage_for_guests_increment / 100)
    return adjusted_nights_rates_breakdown_for_room



