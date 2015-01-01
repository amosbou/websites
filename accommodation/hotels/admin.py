from django.contrib import admin

# Register your models here.

from django.contrib import admin
from hotels.models import Hotel, Room


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