from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns(
    '',
    url(r'^users/', include('users.urls')),
    url(r'^accountancy/', include('accountancy.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^login$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout$', 'django.contrib.auth.views.logout', {'template_name': 'registration/login.html'}),    
)
