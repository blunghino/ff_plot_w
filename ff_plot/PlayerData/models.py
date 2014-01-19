from django.db import models

class Player(models.Model):
	picture = models.ImageField()
	first_name = models.CharField()
	last_name = models.CharField()
	height = models.PositiveSmallIntegerField()
	weight = models.PositiveSmallIntegerField()
	dob = models.DateField()
	yards = models.IntegerField()
	attempts = models.PositiveIntegerField()
	
	
class Season(models.Model):
	player = models.ForeignKey(Player)
	number = models.PositiveSmallIntegerField()
	yards = models.SmallIntegerField()
	attempts = models.SmallIntegerField()
	
	