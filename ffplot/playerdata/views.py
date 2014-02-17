from django.shortcuts import render
from django.views import generic

from .models import RbPlayer, RbSeason, RbGame


class PlayersIndexView(generic.ListView):
	template_name = 'playerdata/base_playerdata.html'
	context_object_name = 'players_list'
	
	def get_queryset(self):
		return RbPlayer.objects.order_by('last_name')
	

def careerdataview(request, urlslug):
	player = RbPlayer.objects.get(urlslug=urlslug)
	seasons = player.rbseason_set.all()
	career_field_names = ['career_rushing_attempts', 'career_rushing_yards', 
							'career_receptions', 'career_receiving_yards', ]
	career_field_data = [getattr(player, f) for f in career_field_names]
	season_field_names = ['year', 'season_rushing_attempts', 'season_rushing_yards']
	season_field_data = [[getattr(s, f) for f in season_field_names] for s in seasons]
	template_name = 'playerdata/playerdata_career_data.html'
	context = {
				'player': player, 			
				'career_field_names': career_field_names, 
				'career_field_data': career_field_data, 
				'season_field_names': season_field_names, 
				'season_field_data': season_field_data,
				'season_field_numbers': list(range(len(season_field_names))),
		}
	return render(request, template_name, context)
	
	
def seasondataview(request, urlslug, year):
	template_name = 'playerdata/playerdata_season_data.html'
	context = {'year': year}
	return render(request, template_name, context)
	
	
# class SeasonDataView(generic.DetailView):
# 	template_name = 'playerdata/playerdata_season_data.html'
# 	player = RbPlayer.objects.get(last_name=player_name)
# 	season = player.rbseason_set.get(year_string=year_string)
	
	
