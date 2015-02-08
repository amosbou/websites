from django.conf.urls import patterns, url

from hotels import views

urlpatterns = patterns('',
                        url(r'^$', views.index, name='index'),
                        url(r'^index.html$', views.index, name='index'),
                        url(r'^three-room-list.html$', views.three_rooms_list, name='three_rooms_list'),
                        url(r'^two-columns-rooms-list.html$', views.two_columns_rooms_list, name='two_columns_rooms_list'),
                        url(r'(?P<room_id>\d+)/room-with-one-bedroom.html$', views.room_with_one_bedroom,
                            name='room_with_one_bedroom'),
                        url(r'^choose-date-page/$', views.choose_date_page,
                            name='choose_date_page'),
                        url(r'(?P<room_id>\d+)/choose-room-page/$', views.choose_room_page,
                            name='choose_room_page'),
                        url(r'choose-room-page/$', views.choose_room_page,
                            name='choose_room_page'),
                        url(r'(?P<room_id>\d+)/checkout/$', views.checkout,
                            name='checkout'),
                       )
