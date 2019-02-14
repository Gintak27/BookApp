"""
Definition of urls for BookApp.
"""

from django.conf.urls import include, url
from BookApp import Home
from BookApp.Home.views import index
import BookApp
from BookApp.Home import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    # Examples:
     url(r'^$', Home.views.index, name='index'),
     url(r'^home$', Home.views.index, name='home'),
    # url(r'^$', BookApp.views.home, name='home'),
    # url(r'^BookApp/', include('BookApp.BookApp.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
]
