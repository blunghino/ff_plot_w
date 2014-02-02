# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'RbPlayer.n_seasons'
        db.add_column('playerdata_rbplayer', 'n_seasons',
                      self.gf('django.db.models.fields.PositiveSmallIntegerField')(blank=True, null=True),
                      keep_default=False)

        # Adding field 'RbSeason.games_played'
        db.add_column('playerdata_rbseason', 'games_played',
                      self.gf('django.db.models.fields.PositiveSmallIntegerField')(blank=True, null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'RbPlayer.n_seasons'
        db.delete_column('playerdata_rbplayer', 'n_seasons')

        # Deleting field 'RbSeason.games_played'
        db.delete_column('playerdata_rbseason', 'games_played')


    models = {
        'playerdata.rbgame': {
            'Meta': {'object_name': 'RbGame'},
            'game_date': ('django.db.models.fields.DateField', [], {'blank': 'True', 'null': 'True'}),
            'game_rushing_attempts': ('django.db.models.fields.PositiveSmallIntegerField', [], {'blank': 'True', 'null': 'True'}),
            'game_rushing_yards': ('django.db.models.fields.SmallIntegerField', [], {'blank': 'True', 'null': 'True'}),
            'home_game': ('django.db.models.fields.NullBooleanField', [], {'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'opponent': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True', 'null': 'True'}),
            'season': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['playerdata.RbSeason']"})
        },
        'playerdata.rbplayer': {
            'Meta': {'object_name': 'RbPlayer'},
            'career_receiving_yards': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'career_receptions': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'career_rushing_attempts': ('django.db.models.fields.PositiveIntegerField', [], {'blank': 'True', 'null': 'True'}),
            'career_rushing_yards': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'college': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True', 'null': 'True'}),
            'dob': ('django.db.models.fields.DateField', [], {'blank': 'True', 'null': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True', 'null': 'True'}),
            'headshot': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True', 'null': 'True'}),
            'height': ('django.db.models.fields.PositiveSmallIntegerField', [], {'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True', 'null': 'True'}),
            'n_seasons': ('django.db.models.fields.PositiveSmallIntegerField', [], {'blank': 'True', 'null': 'True'}),
            'position': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True', 'null': 'True'}),
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
            'year_range': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True', 'null': 'True'})
        }
    }

    complete_apps = ['playerdata']