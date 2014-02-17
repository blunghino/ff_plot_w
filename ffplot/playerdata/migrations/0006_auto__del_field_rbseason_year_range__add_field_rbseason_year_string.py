# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'RbSeason.year_range'
        db.delete_column('playerdata_rbseason', 'year_range')

        # Adding field 'RbSeason.year_string'
        db.add_column('playerdata_rbseason', 'year_string',
                      self.gf('django.db.models.fields.CharField')(blank=True, null=True, max_length=4),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'RbSeason.year_range'
        db.add_column('playerdata_rbseason', 'year_range',
                      self.gf('django.db.models.fields.CharField')(blank=True, null=True, max_length=20),
                      keep_default=False)

        # Deleting field 'RbSeason.year_string'
        db.delete_column('playerdata_rbseason', 'year_string')


    models = {
        'playerdata.rbgame': {
            'Meta': {'object_name': 'RbGame'},
            'game_date': ('django.db.models.fields.DateField', [], {'blank': 'True', 'null': 'True'}),
            'game_rushing_attempts': ('django.db.models.fields.PositiveSmallIntegerField', [], {'blank': 'True', 'null': 'True'}),
            'game_rushing_yards': ('django.db.models.fields.SmallIntegerField', [], {'blank': 'True', 'null': 'True'}),
            'home_game': ('django.db.models.fields.NullBooleanField', [], {'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'opponent': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '50'}),
            'season': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['playerdata.RbSeason']"})
        },
        'playerdata.rbplayer': {
            'Meta': {'object_name': 'RbPlayer'},
            'career_receiving_yards': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'career_receptions': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'career_rushing_attempts': ('django.db.models.fields.PositiveIntegerField', [], {'blank': 'True', 'null': 'True'}),
            'career_rushing_yards': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'college': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '100'}),
            'dob': ('django.db.models.fields.DateField', [], {'blank': 'True', 'null': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '50'}),
            'headshot': ('django.db.models.fields.files.ImageField', [], {'blank': 'True', 'null': 'True', 'max_length': '100'}),
            'height': ('django.db.models.fields.PositiveSmallIntegerField', [], {'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '50'}),
            'n_seasons': ('django.db.models.fields.PositiveSmallIntegerField', [], {'blank': 'True', 'null': 'True'}),
            'position': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '50'}),
            'weight': ('django.db.models.fields.PositiveSmallIntegerField', [], {'blank': 'True', 'null': 'True'})
        },
        'playerdata.rbseason': {
            'Meta': {'object_name': 'RbSeason'},
            'games_played': ('django.db.models.fields.PositiveSmallIntegerField', [], {'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.PositiveSmallIntegerField', [], {'blank': 'True', 'null': 'True'}),
            'player': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['playerdata.RbPlayer']"}),
            'season_rushing_attempts': ('django.db.models.fields.PositiveSmallIntegerField', [], {'blank': 'True', 'null': 'True'}),
            'season_rushing_yards': ('django.db.models.fields.SmallIntegerField', [], {'blank': 'True', 'null': 'True'}),
            'year_string': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '4'})
        }
    }

    complete_apps = ['playerdata']