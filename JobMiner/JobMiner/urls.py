from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url('^$', 'fetch.views.home_page', name='home_page'),
    url(r'^admin/', include(admin.site.urls)),
)