from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', 'clothes.views.landing'),
    (r'^pants4thunderthighs/',        include('clothes.urls')),
#    (r'^search/$', 'clothes.views.home'),
 #   (r'^results/$', 'clothes.views.results'),
	#(r'^product_info/$', 'clothes.views.product_info'),
	#(r'^about/$', 'clothes.views.about'),
	#(r'^compare/$', 'clothes.views.compare'),
	#(r'^logout/$', 'clothes.views.logout'),
	#(r'^create/$', 'clothes.views.create'),
	# url(r'^clothesliner/', include('clothesliner.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('django.contrib.staticfiles.views',
    url(r'^static/(?P<path>.*)$', 'serve', kwargs={"insecure": True}),
)
