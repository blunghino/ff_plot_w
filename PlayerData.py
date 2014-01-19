from django.db import models

class Player(models.Model):
	picture = models.ImageField()
	season1 = Season()
	season2 = Season()
	seasons = [season1, season2]
	first_name = models.CharField()
	last_name = models.CharField()
	height = models.PositiveSmallIntegerField()
	weight = models.PositiveSmallIntegerField()
	dob = models.DateField()
	yards
	attempts
	yards_after_contact
	
class Season(models.Model):
	player = models.ForeignKey(Player)
	game1 = Game(season)
	game2 
	game3
	team
	number = models.PositiveSmallIntegerField()
	yards = 1200
	attempts
	yards_after_contact
	
class Game(models.Model):
	playoff
	attempts
	yards
	td
	opponent