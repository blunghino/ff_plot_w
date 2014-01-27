from django.db import models

from core.models import PlayerModel, SeasonModel, GameModel


class RbPlayer(PlayerModel):
	"""
	career level data for running backs
	"""
	career_rushing_yards = models.IntegerField(null=True, blank=True)
	career_rushing_attempts = models.PositiveIntegerField(null=True, blank=True)
	
# 	def __str__(self):
# 		return self.first_name + ' ' + self.last_name
	
	
class RbSeason(SeasonModel):
	"""
	single season data for running backs
	"""
	player = models.ForeignKey(RbPlayer)
# 	team = models.ForeignKey(TeamSeason)
	season_rushing_yards = models.SmallIntegerField(null=True, blank=True)
	season_rushing_attempts = models.PositiveSmallIntegerField(null=True, blank=True)
	
# 	def __str__(self):
# 		return self.player.first_name + ' ' + self.player.last_name + ': ' + str(yards)
	
	
class RbGame(GameModel):
	"""
	single game data for running backs
	"""
	season = models.ForeignKey(RbSeason)
# 	game = models.ForeignKey(TeamGame)
# 	opponent = models.ForeignKey(TeamSeason)
	game_rushing_yards = models.SmallIntegerField(null=True, blank=True)
	game_rushing_attempts = models.PositiveSmallIntegerField(null=True, blank=True)
	
	
# class QbPlayer(PlayerModel):
# 	"""
# 	career level data for quarterbacks
# 	"""
# 	passing_yards= models.IntegerField(null=True, blank=True)
# 	passing_attempts = models.PositiveIntegerField(null=True, blank=True)