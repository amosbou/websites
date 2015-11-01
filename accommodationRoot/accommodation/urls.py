from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
                        # Examples:
                        # url(r'^$', 'accommodation.views.home', name='home'),
                        # url(r'^blog/', include('blog.urls')),

                        url(r'^hotels/', include('hotels.urls', namespace="hotels")),
                        url(r'^admin/', include(admin.site.urls)),
)
