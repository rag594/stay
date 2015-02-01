from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'stay.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^stayz/',include('stayz.urls')),

    url(r'^stayz/st',include('stayz.urls1')),
    url(r'^admin/', include(admin.site.urls)),
)
