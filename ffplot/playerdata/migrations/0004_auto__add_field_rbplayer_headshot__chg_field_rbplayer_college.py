# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'RbPlayer.headshot'
        db.add_column('playerdata_rbplayer', 'headshot',
                      self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True),
                      keep_default=False)


        # Changing field 'RbPlayer.college'
        db.alter_column('playerdata_rbplayer', 'college', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

    def backwards(self, orm):
        # Deleting field 'RbPlayer.headshot'
        db.delete_column('playerdata_rbplayer', 'headshot')


        # Changing field 'RbPlayer.college'
        db.alter_column('playerdata_rbplayer', 'college', self.gf('django.db.models.fields.CharField')(null=True, max_length=50))

    models = {
        'playerdata.rbgame': {
            'Meta': {'object_name': 'RbGame'},
            'game_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'game_rushing_attempts': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'game_rushing_yards': ('django.db.models.fields.SmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'home_game': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'opponent': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'season': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['playerdata.RbSeason']"})
        },
        'playerdata.rbplayer': {
            'Meta': {'object_name': 'RbPlayer'},
            'career_receiving_yards': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'career_receptions': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'career_rushing_attempts': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'career_rushing_yards': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'college': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'dob': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'headshot': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'height': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'position': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'weight': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'playerdata.rbseason': {
            'Meta': {'object_name': 'RbSeason'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'player': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['playerdata.RbPlayer']"}),
            'season_rushing_attempts': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'season_rushing_yards': ('django.db.models.fields.SmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'year_range': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['playerdata']