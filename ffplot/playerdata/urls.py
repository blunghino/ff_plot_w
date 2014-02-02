from django.conf.urls import patterns, url

from playerdata import views

urlpatterns = patterns('', 
						url(r'^$', views.index, name='players index'),
						url(r'^(?P<player_name>\w+)/$', views.career_detail, name='career detail'),
)