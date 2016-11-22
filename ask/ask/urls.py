from django.conf.urls import patterns, include, url

from django.contrib import admin
from qa.views import  test
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^question/$', test),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^question/$', include(qa.urls)),
)
