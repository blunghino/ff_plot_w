from django.test import TestCase
from django.core.urlresolvers import reverse

from playerdata.models import RbPlayer


def create_rbplayer(last_name='McKringleberry', first_name='Hingle', career_receptions=1000):
	"""
	create an RbPlayer object with last_name and career_receptions fields populated
	"""
	return RbPlayer.objects.create(last_name=last_name, 
									first_name=first_name,
							    	career_receptions=career_receptions)


class RbPlayerViewTests(TestCase):
	def test_playersindexview_with_no_players(self):
		"""
		if no players exist, no context data is provided
		"""
		response = self.client.get(reverse('playerdata:players_index'))
		self.assertEqual(response.status_code, 200)
		self.assertQuerysetEqual(response.context['players_list'], [])

	def test_playersindexview_with_players(self):
		"""
		if players exist, their attributes can be accessed through context data
		"""
		create_rbplayer()
		create_rbplayer('Eeeeeeee', 'Eeee', career_receptions=10)
		response = self.client.get(reverse('playerdata:players_index'))
		self.assertQuerysetEqual(
								 [p.career_receptions for p in response.context['players_list']],
								 ['10', '1000']		 
								 )


class CareerdataviewTests(TestCase):
	def test_careerdataview_with_invalid_player(self):
		"""
		if a player who does not exist is requested, redirect to a player not found page
		"""
		pass
		
		
	def test_careerdataview_with_player_with_partial_data(self):
		"""
		if a player who has only some data is requested, that data exists and other 
		fields still exist but are empty
		"""
		player = create_rbplayer()
		response = self.client.get(reverse('playerdata:career_data', 
										   kwargs={'player_name': player.last_name}))
		self.assertEqual(response.context['player'].last_name, 'McKringleberry')
		self.assertEqual(response.context['field_names'],  
						 ['career_rushing_yards', 'career_rushing_attempts', 
						 'career_receiving_yards', 'career_receptions'])
		self.assertEqual(response.context['field_data'][3], 1000)
		self.assertIsNone(response.context['field_data'][0])