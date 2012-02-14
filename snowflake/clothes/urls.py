from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$',        'clothes.views.home'),
    (r'^search/$', 'clothes.views.home'),
    (r'^results/$', 'clothes.views.results'),
    (r'^reference/$', 'clothes.views.find_reference'),
	(r'^super_compare/(?P<comp>\d+)/$', 'clothes.views.super_compare'),
	(r'^super_compare/$', 'clothes.views.super_compare'),
    (r'^about/$', 'clothes.views.about'),
    (r'^create/$', 'clothes.views.create'),
)

urlpatterns += patterns('django.contrib.staticfiles.views',
    url(r'^static/(?P<path>.*)$', 'serve', kwargs={"insecure": True}),
)

