from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'landing.views.home', name='home'),
    url(r'^submit/$', 'landing.views.submit', name='submit'),
)
