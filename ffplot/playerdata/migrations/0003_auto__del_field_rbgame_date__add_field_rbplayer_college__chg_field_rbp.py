# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'RbGame.date'
        db.delete_column('playerdata_rbgame', 'date')

        # Adding field 'RbPlayer.college'
        db.add_column('playerdata_rbplayer', 'college',
                      self.gf('django.db.models.fields.CharField')(blank=True, null=True, max_length=50),
                      keep_default=False)


        # Changing field 'RbPlayer.position'
        db.alter_column('playerdata_rbplayer', 'position', self.gf('django.db.models.fields.CharField')(null=True, max_length=50))

        # Changing field 'RbPlayer.first_name'
        db.alter_column('playerdata_rbplayer', 'first_name', self.gf('django.db.models.fields.CharField')(null=True, max_length=50))

        # Changing field 'RbPlayer.last_name'
        db.alter_column('playerdata_rbplayer', 'last_name', self.gf('django.db.models.fields.CharField')(null=True, max_length=50))

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'RbGame.date'
        raise RuntimeError("Cannot reverse this migration. 'RbGame.date' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'RbGame.date'
        db.add_column('playerdata_rbgame', 'date',
                      self.gf('django.db.models.fields.DateField')(),
                      keep_default=False)

        # Deleting field 'RbPlayer.college'
        db.delete_column('playerdata_rbplayer', 'college')


        # User chose to not deal with backwards NULL issues for 'RbPlayer.position'
        raise RuntimeError("Cannot reverse this migration. 'RbPlayer.position' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'RbPlayer.position'
        db.alter_column('playerdata_rbplayer', 'position', self.gf('django.db.models.fields.CharField')(max_length=50))

        # User chose to not deal with backwards NULL issues for 'RbPlayer.first_name'
        raise RuntimeError("Cannot reverse this migration. 'RbPlayer.first_name' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'RbPlayer.first_name'
        db.alter_column('playerdata_rbplayer', 'first_name', self.gf('django.db.models.fields.CharField')(max_length=50))

        # User chose to not deal with backwards NULL issues for 'RbPlayer.last_name'
        raise RuntimeError("Cannot reverse this migration. 'RbPlayer.last_name' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'RbPlayer.last_name'
        db.alter_column('playerdata_rbplayer', 'last_name', self.gf('django.db.models.fields.CharField')(max_length=50))

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
            'college': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '50'}),
            'dob': ('django.db.models.fields.DateField', [], {'blank': 'True', 'null': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '50'}),
            'height': ('django.db.models.fields.PositiveSmallIntegerField', [], {'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '50'}),
            'position': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '50'}),
            'weight': ('django.db.models.fields.PositiveSmallIntegerField', [], {'blank': 'True', 'null': 'True'})
        },
        'playerdata.rbseason': {
            'Meta': {'object_name': 'RbSeason'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.PositiveSmallIntegerField', [], {'blank': 'True', 'null': 'True'}),
            'player': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['playerdata.RbPlayer']"}),
            'season_rushing_attempts': ('django.db.models.fields.PositiveSmallIntegerField', [], {'blank': 'True', 'null': 'True'}),
            'season_rushing_yards': ('django.db.models.fields.SmallIntegerField', [], {'blank': 'True', 'null': 'True'}),
            'year_range': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '20'})
        }
    }

    complete_apps = ['playerdata']