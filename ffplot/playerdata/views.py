from django.shortcuts import render
from django.views import generic

from .models import RbPlayer, RbSeason, RbGame


class PlayersIndexView(generic.ListView):
	template_name = 'playerdata/base_playerdata.html'
	context_object_name = 'players_list'
	
	def get_queryset(self):
		return RbPlayer.objects.order_by('last_name')
	

def career_data_view(request, urlslug):
	position = urlslug.split('_')[-1].lower()
	season_field_names = ['year']
	if position == 'rb':
		player = RbPlayer.objects.get(urlslug=urlslug)
		seasons = player.rbseason_set.all()
		career_field_names = ['career_rushing_attempts', 'career_rushing_yards', 
							'career_receptions', 'career_receiving_yards', ]
		season_field_names += ['season_rushing_attempts', 'season_rushing_yards']
#	elif position = 'wr':
#		player = WrPlayer.objects.get(urlslug=urlslug)... etc
#	else:
#		return some error or 404
	career_field_data = [getattr(player, f) for f in career_field_names]
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
	
	
def season_data_view(request, urlslug, year):
	position = urlslug.split('_')[-1].lower()
	season_field_names = ['year']
	game_field_names = ['game_date', 'opponent', 'home_game']
	if position == 'rb':
		player = RbPlayer.objects.get(urlslug=urlslug)
		season = player.rbseason_set.get(year=year)
		games = season.rbgame_set.all()
		season_field_names += ['season_rushing_attempts', 'season_rushing_yards']
		game_field_names += ['game_rushing_attempts', 'game_rushing_yards']
	season_field_data = [getattr(season, f) for f in season_field_names]
	game_field_data = [[getattr(g, f) for f in game_field_names] for g in games]
	template_name = 'playerdata/playerdata_season_data.html'
	context = {
				'season': season,
				'season_field_names': season_field_names,
				'season_field_data': season_field_data,
				'game_field_names': game_field_names,
				'game_field_data': game_field_data,
		}
	return render(request, template_name, context)
	
	
# class RbSeasonDataView(generic.DetailView):
# 	template_name = 'playerdata/playerdata_season_data.html'
# 	player = RbPlayer.objects.get(urlslug=urlslug)
# 	season = player.rbseason_set.get(year=year)
	
	
