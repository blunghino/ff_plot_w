# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'RbPlayer.career_receiving_yards'
        db.add_column('playerdata_rbplayer', 'career_receiving_yards',
                      self.gf('django.db.models.fields.IntegerField')(blank=True, null=True),
                      keep_default=False)

        # Adding field 'RbPlayer.career_receptions'
        db.add_column('playerdata_rbplayer', 'career_receptions',
                      self.gf('django.db.models.fields.IntegerField')(blank=True, null=True),
                      keep_default=False)

        # Adding field 'RbGame.game_date'
        db.add_column('playerdata_rbgame', 'game_date',
                      self.gf('django.db.models.fields.DateField')(blank=True, null=True),
                      keep_default=False)

        # Adding field 'RbGame.home_game'
        db.add_column('playerdata_rbgame', 'home_game',
                      self.gf('django.db.models.fields.NullBooleanField')(blank=True, null=True),
                      keep_default=False)

        # Adding field 'RbGame.opponent'
        db.add_column('playerdata_rbgame', 'opponent',
                      self.gf('django.db.models.fields.CharField')(blank=True, max_length=50, null=True),
                      keep_default=False)

        # Adding field 'RbSeason.year_range'
        db.add_column('playerdata_rbseason', 'year_range',
                      self.gf('django.db.models.fields.CharField')(blank=True, max_length=20, null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'RbPlayer.career_receiving_yards'
        db.delete_column('playerdata_rbplayer', 'career_receiving_yards')

        # Deleting field 'RbPlayer.career_receptions'
        db.delete_column('playerdata_rbplayer', 'career_receptions')

        # Deleting field 'RbGame.game_date'
        db.delete_column('playerdata_rbgame', 'game_date')

        # Deleting field 'RbGame.home_game'
        db.delete_column('playerdata_rbgame', 'home_game')

        # Deleting field 'RbGame.opponent'
        db.delete_column('playerdata_rbgame', 'opponent')

        # Deleting field 'RbSeason.year_range'
        db.delete_column('playerdata_rbseason', 'year_range')


    models = {
        'playerdata.rbgame': {
            'Meta': {'object_name': 'RbGame'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'game_date': ('django.db.models.fields.DateField', [], {'blank': 'True', 'null': 'True'}),
            'game_rushing_attempts': ('django.db.models.fields.PositiveSmallIntegerField', [], {'blank': 'True', 'null': 'True'}),
            'game_rushing_yards': ('django.db.models.fields.SmallIntegerField', [], {'blank': 'True', 'null': 'True'}),
            'home_game': ('django.db.models.fields.NullBooleanField', [], {'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'opponent': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '50', 'null': 'True'}),
            'season': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['playerdata.RbSeason']"})
        },
        'playerdata.rbplayer': {
            'Meta': {'object_name': 'RbPlayer'},
            'career_receiving_yards': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'career_receptions': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'career_rushing_attempts': ('django.db.models.fields.PositiveIntegerField', [], {'blank': 'True', 'null': 'True'}),
            'career_rushing_yards': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'dob': ('django.db.models.fields.DateField', [], {'blank': 'True', 'null': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'height': ('django.db.models.fields.PositiveSmallIntegerField', [], {'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'position': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'weight': ('django.db.models.fields.PositiveSmallIntegerField', [], {'blank': 'True', 'null': 'True'})
        },
        'playerdata.rbseason': {
            'Meta': {'object_name': 'RbSeason'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.PositiveSmallIntegerField', [], {'blank': 'True', 'null': 'True'}),
            'player': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['playerdata.RbPlayer']"}),
            'season_rushing_attempts': ('django.db.models.fields.PositiveSmallIntegerField', [], {'blank': 'True', 'null': 'True'}),
            'season_rushing_yards': ('django.db.models.fields.SmallIntegerField', [], {'blank': 'True', 'null': 'True'}),
            'year_range': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '20', 'null': 'True'})
        }
    }

    complete_apps = ['playerdata']