from django.conf.urls import patterns, url

from hotels import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^index.html$', views.index, name='index'),
    url(r'^three-room-list.html$', views.three_rooms_list, name='three_rooms_list'),
    url(r'^two-columns-rooms-list.html$', views.two_columns_rooms_list, name='two_columns_rooms_list'),
    url(r'(?P<room_id>\d+)/room-with-one-bedroom.html$', views.room_with_one_bedroom, name='room_with_one_bedroom'),
    url(r'^reservation-page-2-2.html$', views.reservation_page_2_2, name='reservation_page_2_2'),
    url(r'(?P<hotel_id>\d+)/(?P<room_id>\d+)/$', views.room_details, name='room_details'),
    url(r'(?P<hotel_id>\d+)/(?P<room_id>\d+)/reservation$', views.reservation_form, name='reservation_form'),

)