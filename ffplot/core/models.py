from django.db import models


class TimeStampedModel(models.Model):
	"""
	an abstract base class that provides self-updating "created" and "modified" fields
	"""
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)
	
	class Meta:
		abstract = True

		
class PlayerModel(models.Model):
	"""
	an abstract base class: career data fields applicable to all player positions
	"""
# 	headshot = models.ImageField(upload_to='player_headshots', null=True, blank=True)
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	position = models.CharField(max_length=50)
	height = models.PositiveSmallIntegerField(null=True, blank=True)
	weight = models.PositiveSmallIntegerField(null=True, blank=True)
	dob = models.DateField(null=True, blank=True)
	
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
	date = models.DateField()
	
	class Meta:
		abstract = True