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
	template_name = 'playerdata/playerdata_career_data.html'
	context = {'player': player}
	return render(request, template_name, context)
	
