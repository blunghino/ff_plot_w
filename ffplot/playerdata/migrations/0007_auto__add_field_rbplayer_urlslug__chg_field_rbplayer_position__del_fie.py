# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'RbPlayer.urlslug'
        db.add_column('playerdata_rbplayer', 'urlslug',
                      self.gf('django.db.models.fields.SlugField')(blank=True, max_length=50, null=True),
                      keep_default=False)


        # Changing field 'RbPlayer.position'
        db.alter_column('playerdata_rbplayer', 'position', self.gf('django.db.models.fields.CharField')(max_length=2, null=True))
        # Deleting field 'RbSeason.year_string'
        db.delete_column('playerdata_rbseason', 'year_string')

        # Adding field 'RbSeason.year'
        db.add_column('playerdata_rbseason', 'year',
                      self.gf('django.db.models.fields.PositiveSmallIntegerField')(blank=True, null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'RbPlayer.urlslug'
        db.delete_column('playerdata_rbplayer', 'urlslug')


        # Changing field 'RbPlayer.position'
        db.alter_column('playerdata_rbplayer', 'position', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))
        # Adding field 'RbSeason.year_string'
        db.add_column('playerdata_rbseason', 'year_string',
                      self.gf('django.db.models.fields.CharField')(blank=True, max_length=4, null=True),
                      keep_default=False)

        # Deleting field 'RbSeason.year'
        db.delete_column('playerdata_rbseason', 'year')


    models = {
        'playerdata.rbgame': {
            'Meta': {'object_name': 'RbGame'},
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
            'college': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '100', 'null': 'True'}),
            'dob': ('django.db.models.fields.DateField', [], {'blank': 'True', 'null': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '50', 'null': 'True'}),
            'headshot': ('django.db.models.fields.files.ImageField', [], {'blank': 'True', 'max_length': '100', 'null': 'True'}),
            'height': ('django.db.models.fields.PositiveSmallIntegerField', [], {'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '50', 'null': 'True'}),
            'n_seasons': ('django.db.models.fields.PositiveSmallIntegerField', [], {'blank': 'True', 'null': 'True'}),
            'position': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '2', 'null': 'True'}),
            'urlslug': ('django.db.models.fields.SlugField', [], {'blank': 'True', 'max_length': '50', 'null': 'True'}),
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
            'year': ('django.db.models.fields.PositiveSmallIntegerField', [], {'blank': 'True', 'null': 'True'})
        }
    }

    complete_apps = ['playerdata']