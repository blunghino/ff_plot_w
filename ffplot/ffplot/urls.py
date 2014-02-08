from django.conf.urls import patterns, include, url

from django.contrib import admin

import playerdata.urls

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ffplot.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^playerdata/', include(playerdata.urls, namespace='playerdata')),
    url(r'^admin/', include(admin.site.urls)),
)
