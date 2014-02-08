from django.conf.urls import patterns, url

from playerdata import views

urlpatterns = patterns('', 
	url(r'^$', views.PlayersIndexView.as_view(), name='players_index'),
	url(r'^(?P<player_name>\w+)/$', views.careerdataview, name='career_data'),
)