from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$',        'clothes.views.home'),
    (r'^search/$', 'clothes.views.home'),
    (r'^results/$', 'clothes.views.results'),
    (r'^reference/$', 'clothes.views.find_reference'),
    (r'^product_info/(?P<comp>\d+)/$', 'clothes.views.product_info'),
    (r'^about/$', 'clothes.views.about'),
    (r'^compare/$', 'clothes.views.compare'),
    (r'^logout/$', 'clothes.views.logout'),
    (r'^create/$', 'clothes.views.create'),
)

urlpatterns += patterns('django.contrib.staticfiles.views',
    url(r'^static/(?P<path>.*)$', 'serve', kwargs={"insecure": True}),
)

