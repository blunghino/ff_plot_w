from django.shortcuts import render
from django.http import HttpResponse

from .models import RbPlayer

def index(request):
	players_list = RbPlayer.objects.order_by('-last_name')
	template_name = 'playerdata/base_playerdata.html'
	context = {'players_list': players_list}
	return render(request, template_name, context)
	
def career_detail(request, player_name):
	return HttpResponse('Career data for %s' % player_name)