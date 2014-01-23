from django.test import TestCase

from ff_plot.PlayerData import Player, Season
from datetime import datetime

p = Player(first_name='Marshawn', last_name='Lynch', dob=datetime.now(), yards=1000,
			attempts=200, height=78, weight=225)

p.season_set.create(yards=400, attempts=75, number=24)

p.season_set.create(yards=600, attempts=125, number=24)

print(Season.objects.filter(player__dob__year=2014))