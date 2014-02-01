from django.db import models

from core.models import PlayerModel, SeasonModel, GameModel
# from teamdata.models import TeamSeason, TeamGame


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
		return 'Rb: %s %s, %s' % (self.year_range, self.player.last_name, 
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
		return 'Rb: vs %s %s, %s' % (self.opponent, self.season.player.last_name, 
									 self.season.player.first_name)
	
	
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