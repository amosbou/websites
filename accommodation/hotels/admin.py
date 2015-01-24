from django.contrib import admin

# Register your models here.

from django.contrib import admin
from hotels.models import Hotel, Room, Booking


class RoomInline(admin.StackedInline):
    model = Room
    extra = 1


class HotelAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name']}),
        ('Details', {'fields': ['city'], 'classes': ['collapse']}),
    ]
    inlines = [RoomInline]
    list_display = ('name', 'city')
    list_filter = ['city']

admin.site.register(Hotel, HotelAdmin)

class BookingInline(admin.StackedInline):
    model = Booking
    extra = 1

class RoomAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name', 'caption', 'type', 'max_num_of_guests',
                                         'description_short', 'rate']}),
        ('Details', {'fields': ['double_bed_size', 'double_bed_num_of', 'single_bed_size',
                                'single_bed_num_of', 'description_long'], 'classes': ['collapse']}),
        ]
    inlines = [BookingInline]
    list_display = ['name', 'description_short']


admin.site.register(Room, RoomAdmin)


class BookingAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['check_in_date', 'check_out_date']}),
        ('Details', {'fields': ['date_created', 'time_created'], 'classes': ['collapse']}),
        ]
    # inlines = [CalendarInLine]
    list_display = ['check_in_date', 'check_out_date']


admin.site.register(Booking, BookingAdmin)
