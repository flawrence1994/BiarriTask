"""
Definition of urls for BiarriTask.
"""

from datetime import datetime
from django.conf.urls import url, include
from django.contrib.auth.models import User
import django.contrib.auth.views

import app.forms
import app.views

# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r'^$', app.views.apitest, name='apitest'),
    #url(r'^apitest', app.views.apitest, name='apitest'),
    url(r'^speakers/$', app.views.SpeakerView.as_view()),
    url(r'^speakers/?((?P<key>[\w]+)=?(?P<value>[\w\s]+))/$', app.views.SpeakerView.as_view()),
    url(r'^plays/$', app.views.PlayView.as_view()),
    url(r'^plays/?((?P<key>[\w]+)=?(?P<value>[\w\s]+))/$', app.views.PlayView.as_view()),
    url(r'^lines/$', app.views.LineView.as_view()),
    url(r'^lines/(?P<limit>[\d]+)/$', app.views.LineView.as_view()),
    url(r'^lines/?((?P<key>[\w]+)=?(?P<value>[\w\s.]+))/$', app.views.LineView.as_view()),
#    url(r'^contact$', app.views.contact, name='contact'),
#    url(r'^about', app.views.about, name='about'),
#    url(r'^login/$',
#        django.contrib.auth.views.login,
#        {
#            'template_name': 'app/login.html',
#            'authentication_form': app.forms.BootstrapAuthenticationForm,
#            'extra_context':
#            {
#                'title': 'Log in',
#                'year': datetime.now().year,
#            }
#        },
#        name='login'),
#    url(r'^logout$',
#        django.contrib.auth.views.logout,
#        {
#            'next_page': '/',
#        },
#        name='logout'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
]
