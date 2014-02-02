from django.db import models

# from .managers import PlayerManager, SeasonManager, GameManager
# from teamdata.models import TeamSeason, TeamGame


## ABSTRACT BASE CLASSES
		
class PlayerModel(models.Model):
	"""
	an abstract base class: career data fields applicable to all player positions
	"""
	headshot = models.ImageField('headshot', upload_to='player_headshots', null=True, blank=True)
	first_name = models.CharField('first name', max_length=50, null=True, blank=True)
	last_name = models.CharField('last_name', max_length=50, null=True, blank=True)
	position = models.CharField('position', max_length=50, null=True, blank=True)
	height = models.PositiveSmallIntegerField('height in inches', null=True, blank=True)
	weight = models.PositiveSmallIntegerField('weight in pounds', null=True, blank=True)
	dob = models.DateField('date of birth', null=True, blank=True)
	n_seasons = models.PositiveSmallIntegerField('number of seasons', null=True, blank=True)
	college = models.CharField('college', max_length=100, null=True, blank=True)
	
# 	objects = PlayerManager()
	
	class Meta:
		abstract = True
		

class SeasonModel(models.Model):
	"""
	an abstract base class: single season data fields applicable to all player positions
	"""
	number = models.PositiveSmallIntegerField('jersey number', null=True, blank=True)
	games_played = models.PositiveSmallIntegerField('regular season games played', 
													null=True, blank=True)

# 	objects = SeasonManager()

	class Meta:
		abstract = True
	
	
class GameModel(models.Model):
	"""
	an abstract base class: single game data fields applicable to all player positions
	"""
	game_date = models.DateField('game date', null=True, blank=True)
	home_game = models.NullBooleanField('home game', null=True, blank=True)
	opponent = models.CharField('opponent', max_length=50, null=True, blank=True)	
# 	day_of_week = models.CharField('day of week', max_length=10, null=True, blank=True)
	
# 	objects = GameManager()
	
	class Meta:
		abstract = True
		
		
## RB CLASSES

class RbPlayer(PlayerModel):
	"""
	career data for running backs
	"""
	career_rushing_yards = models.IntegerField('career rushing yards', null=True, 
										    	blank=True)
	career_rushing_attempts = models.PositiveIntegerField('career rushing attempts',
														  null=True, blank=True)
	career_receiving_yards = models.IntegerField('career receiving yards', null=True, 
												 blank=True)
	career_receptions = models.IntegerField('career receptions', null=True, blank=True)
	
	def __str__(self):
		return 'Rb: %s, %s' % (self.last_name, self.first_name)
	
	
class RbSeason(SeasonModel):
	"""
	single season data for running backs
	"""
	player = models.ForeignKey(RbPlayer)
# 	team = models.ForeignKey(TeamSeason)
	year_range = models.CharField('string of season year range', max_length=20, 
								  null=True, blank=True)
	season_rushing_yards = models.SmallIntegerField('season rushing yards', null=True, 
													blank=True)
	season_rushing_attempts = models.PositiveSmallIntegerField('season rushing attempts',
															   null=True, blank=True)
	
	def __str__(self):
		return 'Rb: %s: %s, %s' % (self.year_range, self.player.last_name, 
							 	  self.player.first_name)
	
	
class RbGame(GameModel):
	"""
	single game data for running backs
	"""
	season = models.ForeignKey(RbSeason)
# 	game = models.ForeignKey(TeamGame)
# 	opponent_season = models.ForeignKey(TeamSeason)
	game_rushing_yards = models.SmallIntegerField('game rushing yards', null=True, 
											    	blank=True)
	game_rushing_attempts = models.PositiveSmallIntegerField('game rushing attempts', 
															 null=True, blank=True)
															 
	def __str__(self):
		return 'Rb: %s vs %s: %s, %s' % (self.game_date, self.opponent, 
										 self.season.player.last_name, 
									     self.season.player.first_name)
	
## QB CLASSES
	
# class QbPlayer(PlayerModel):
# 	"""
# 	career data for quarterbacks
# 	"""
# 	career_passing_yards = models.IntegerField(null=True, blank=True)
# 	career_passing_attempts = models.PositiveIntegerField(null=True, blank=True)
# 	
# 	
# class QbSeason(SeasonModel):
# 	"""
# 	single season data for quarterbacks
# 	"""
# 	player = models.ForeignKey(QbPlayer)
# 	season_passing_yards = models.SmallIntegerField(null=True, blank=True)
# 	season_passing_attempts = models.PositiveSmallIntegerField(null=True, blank=True)
# 	
# 	
# class QbGame(GameModel):
# 	"""
# 	single game data for quarterbacks
# 	"""
# 	season = models.ForeignKey(QbSeason)
# 	game_passing_yards = models.SmallIntegerField(null=True, blank=True)
# 	game_passing_attempts = models.PositiveSmallIntegerField(null=True, blank=True)
# 
# 
# class WrPlayer(PlayerModel):
# 	"""
# 	career data for wide receivers
# 	"""	
# 	