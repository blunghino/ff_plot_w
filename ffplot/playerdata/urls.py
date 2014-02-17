from django.conf.urls import patterns, url

from playerdata import views

urlpatterns = patterns('', 
	url(r'^$', views.PlayersIndexView.as_view(), name='players_index'),
	url(r'^(?P<urlslug>\w+)/$', views.careerdataview, name='career_data'),
	url(r'^(?P<player_name>\w+)/(?P<year>\w+)/$', views.seasondataview, 
		name='season_data'),
)