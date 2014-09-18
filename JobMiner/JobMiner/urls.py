from django.conf.urls import patterns, include, url
from django.contrib import admin

from JobMiner.views import home

admin.autodiscover()

urlpatterns = patterns('',
    url('^$', home, name='home'),
    url('^fetch/', include('fetch.urls')),
    url(r'^admin/', include(admin.site.urls)),
)