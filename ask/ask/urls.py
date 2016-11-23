from django.conf.urls import patterns, include, url

from django.contrib import admin
from qa.views import test
admin.autodiscover()

urlpatterns = patterns('qa.views',
    # Examples:
    # url(r'^question/$', test),
    # url(r'^blog/', include('blog.urls')),/

    url(r'^$', test),
    url(r'^login/', test),
    url(r'^signup/', test),
    url(r'^question/', test),
    url(r'^popular/', test),
    url(r'^ask/', test),
    url(r'^new/', test),
)
