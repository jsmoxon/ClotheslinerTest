from django.conf.urls.defaults import *
from django.contrib import admin
from feedback.models import *
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', 'clothes.views.landing'),
    (r'^demonstration/', include('clothes.urls')),
    (r'^alpha/', include('clothes.urls')),
    (r'^p4tt/', include('clothes.urls')),
    (r'^feedback/$', 'feedback.views.home'),
    (r'^feedback/submit/$', 'feedback.views.feedback_submit'),
    (r'^create/$', 'createpant.views.create'),
    (r'^create/submit/', 'createpant.views.submit'),
    (r'^drawnpantimage/', 'clothes.views.drawnpantimage'),
    (r'^Chris Liem/', 'clothes.views.liemphoto'),
    (r'^register/', 'register.views.register'),
    (r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('django.contrib.staticfiles.views',
    url(r'^static/(?P<path>.*)$', 'serve', kwargs={"insecure": True}),
)
