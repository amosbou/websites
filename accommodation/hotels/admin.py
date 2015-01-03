from django.contrib import admin

# Register your models here.

from django.contrib import admin
from hotels.models import Hotel, Room, Calendar


class RoomInline(admin.StackedInline):
    model = Room
    extra = 1



class HotelAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['hotel_name']}),
        ('Details', {'fields': ['hotel_city'], 'classes': ['collapse']}),
    ]
    inlines = [RoomInline]
    list_display = ('hotel_name', 'hotel_city')
    list_filter = ['hotel_city']

admin.site.register(Hotel, HotelAdmin)


def room_calendar(obj):
    calendar = obj.calendar
    return calendar.calendar_name


class CalendarInLine(admin.StackedInline):
    model = Calendar
    extra = 1


class RoomAdmin(admin.ModelAdmin):
    fields = ('room_name',)
    inlines = [CalendarInLine]
    list_display = ['room_name', room_calendar]


admin.site.register(Room, RoomAdmin)