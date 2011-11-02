from django.conf.urls.defaults import *
from django.contrib import admin
from feedback.models import *
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', 'clothes.views.landing'),
    (r'^pants4thunderthighs/', include('clothes.urls')),
    (r'^feedback/$', 'feedback.views.home'),
    (r'^feedback/submit/$', 'feedback.views.feedback_submit'),
    (r'^create/$', 'createpant.views.create'),
    (r'^create/submit/', 'createpant.views.submit'),

    (r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('django.contrib.staticfiles.views',
    url(r'^static/(?P<path>.*)$', 'serve', kwargs={"insecure": True}),
)
