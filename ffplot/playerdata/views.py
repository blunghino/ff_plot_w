from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse('Index of players')
	
def career_detail(request, player_name):
	return HttpResponse('Career data for %s' % player_name)