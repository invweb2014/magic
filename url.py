from django.conf.urls import patterns, include, url
from route.base import Route

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'xprj.views.home', name='home'),
   
    (r'(?P<node>.+)/', Route.route),
 

)
