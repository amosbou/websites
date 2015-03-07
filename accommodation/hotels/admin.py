from django.contrib import admin

# Register your models here.

from django.contrib import admin
from hotels.models import Hotel, Room, Booking, Guest, Address, GuestAddress, AddressType, Country


class RoomInline(admin.StackedInline):
    model = Room
    extra = 0


class HotelAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name']}),
        ('Details', {'fields': ['city'], 'classes': ['collapse']}),
    ]
    inlines = [RoomInline]
    list_display = ('name', 'city')
    list_filter = ['city']

admin.site.register(Hotel, HotelAdmin)


class BookingInline(admin.TabularInline):
    model = Booking
    extra = 0


class RoomAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name', 'caption', 'type', 'max_num_of_guests',
                                         'description_short', 'rate']}),
        ('Details', {'fields': ['double_bed_size', 'double_bed_num_of', 'single_bed_size',
                                'single_bed_num_of', 'description_long'], 'classes': ['collapse']}),
        ]
    inlines = [BookingInline]
    # list_display = ['name', 'description_short']


admin.site.register(Room, RoomAdmin)


class GuestInline(admin.StackedInline):
    model = Guest
    extra = 0


class BookingAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['room', 'check_in_date', 'check_out_date']}),
        ('Details', {'fields': ['date_created', 'time_created'], 'classes': ['collapse']}),
        ]
    readonly_fields = ('date_created', 'time_created')
    list_display = ['check_in_date', 'check_out_date', 'room', 'guest']
    date_hierarchy = 'check_in_date'


admin.site.register(Booking, BookingAdmin)


class AddressInline(admin.StackedInline):
    model = Address
    extra = 0


class GuestAddressInline(admin.StackedInline):
    model = GuestAddress
    extra = 0


class GuestAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['first_name', 'last_name']})
    ]
    inlines = [BookingInline, GuestAddressInline]


admin.site.register(Guest, GuestAdmin)


class AddressAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['address', 'city','zipcode', 'country']})
    ]


admin.site.register(Address, AddressAdmin)
