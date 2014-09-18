__author__ = 'skambashi'

from django.conf.urls import patterns, url
from fetch.views import home_page

urlpatterns = patterns('',
    url('^$', home_page, name='fetch_home_page'),
)