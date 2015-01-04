from django.conf.urls import patterns, url

from hotels import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^index.html$', views.index, name='index'),
    url(r'^(?P<hotel_id>\d+)/$', views.accommodation, name='accommodation'),
    url(r'(?P<hotel_id>\d+)/(?P<room_id>\d+)/$', views.room_details, name='room_details'),
    url(r'(?P<hotel_id>\d+)/(?P<room_id>\d+)/reservation$', views.reservation_form, name='reservation_form'),

)
