from django.conf.urls import patterns, url

from playerdata import views

urlpatterns = patterns('', 
	url(r'^$', views.PlayersIndexView.as_view(), name='players_index'),
	url(r'^(?P<urlslug>\w+)/$', views.career_data_view, name='career_data'),
	url(r'^(?P<urlslug>\w+)/(?P<year>\w+)/$', views.season_data_view, 
		name='season_data'),
)