from django.db import models

class Player(models.Model):
# 	picture = models.ImageField()
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	height = models.PositiveSmallIntegerField()
	weight = models.PositiveSmallIntegerField()
	dob = models.DateField()
	yards = models.IntegerField()
	attempts = models.PositiveIntegerField()
	
	def __str__(self):
		return self.first_name + ' ' + self.last_name
	
class Season(models.Model):
	player = models.ForeignKey(Player)
	number = models.PositiveSmallIntegerField()
	yards = models.SmallIntegerField()
	attempts = models.SmallIntegerField()
	
	def __str__(self):
		return self.player.first_name + ' ' + self.player.last_name + ': ' + str(yards)
	
	