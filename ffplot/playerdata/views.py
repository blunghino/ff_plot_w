from django.shortcuts import render
from django.views import generic

from .models import RbPlayer


class PlayersIndexView(generic.ListView):
	template_name = 'playerdata/base_playerdata.html'
	context_object_name = 'players_list'
	
	def get_queryset(self):
		return RbPlayer.objects.order_by('last_name')


def index(request):
	players_list = RbPlayer.objects.order_by('last_name')
	template_name = 'playerdata/base_playerdata.html'
	context = {'players_list': players_list}
	return render(request, template_name, context)
	

def careerdataview(request, player_name):
	player = RbPlayer.objects.get(last_name=player_name)
	field_names = ['career_rushing_yards', 'career_rushing_attempts', 
					'career_receiving_yards', 'career_receptions']
	field_data = [getattr(player, f) for f in field_names]
	template_name = 'playerdata/playerdata_career_data.html'
	context = {'player': player, 'field_names': field_names, 'field_data': field_data}
	return render(request, template_name, context)
	
