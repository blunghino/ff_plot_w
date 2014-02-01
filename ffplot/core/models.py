from django.db import models
# 
# 
# class TimeStampedModel(models.Model):
# 	"""
# 	an abstract base class that provides self-updating "created" and "modified" fields
# 	"""
# 	created = models.DateTimeField(auto_now_add=True)
# 	modified = models.DateTimeField(auto_now=True)
# 	
# 	class Meta:
# 		abstract = True

		
class PlayerModel(models.Model):
	"""
	an abstract base class: career data fields applicable to all player positions
	"""
# 	headshot = models.ImageField('headshot', upload_to='player_headshots', null=True, blank=True)
	first_name = models.CharField('first name', max_length=50, null=True)
	last_name = models.CharField('last_name', max_length=50, null=True)
	position = models.CharField('position', max_length=50, null=True, blank=True)
	height = models.PositiveSmallIntegerField('height in inches', null=True, blank=True)
	weight = models.PositiveSmallIntegerField('weight in pounds', null=True, blank=True)
	dob = models.DateField('date of birth', null=True, blank=True)
	college = models.CharField('college', max_length=50, null=True, blank=True)
	
	class Meta:
		abstract = True
		

class SeasonModel(models.Model):
	"""
	an abstract base class: single season data fields applicable to all player positions
	"""
	number = models.PositiveSmallIntegerField(null=True, blank=True)
	
	class Meta:
		abstract = True
	
	
class GameModel(models.Model):
	"""
	an abstract base class: single game data fields applicable to all player positions
	"""
	game_date = models.DateField('game date', null=True, blank=True)
	home_game = models.NullBooleanField('home or away', null=True, blank=True)
	opponent = models.CharField('opponent', max_length=50, null=True, blank=True)	
	
	class Meta:
		abstract = True