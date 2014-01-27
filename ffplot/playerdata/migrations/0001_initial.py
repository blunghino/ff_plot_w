# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'RbPlayer'
        db.create_table('playerdata_rbplayer', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('position', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('height', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True)),
            ('weight', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True)),
            ('dob', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('career_rushing_yards', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('career_rushing_attempts', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('playerdata', ['RbPlayer'])

        # Adding model 'RbSeason'
        db.create_table('playerdata_rbseason', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('number', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True)),
            ('player', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['playerdata.RbPlayer'])),
            ('season_rushing_yards', self.gf('django.db.models.fields.SmallIntegerField')(null=True, blank=True)),
            ('season_rushing_attempts', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('playerdata', ['RbSeason'])

        # Adding model 'RbGame'
        db.create_table('playerdata_rbgame', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('season', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['playerdata.RbSeason'])),
            ('game_rushing_yards', self.gf('django.db.models.fields.SmallIntegerField')(null=True, blank=True)),
            ('game_rushing_attempts', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('playerdata', ['RbGame'])


    def backwards(self, orm):
        # Deleting model 'RbPlayer'
        db.delete_table('playerdata_rbplayer')

        # Deleting model 'RbSeason'
        db.delete_table('playerdata_rbseason')

        # Deleting model 'RbGame'
        db.delete_table('playerdata_rbgame')


    models = {
        'playerdata.rbgame': {
            'Meta': {'object_name': 'RbGame'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'game_rushing_attempts': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'game_rushing_yards': ('django.db.models.fields.SmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'season': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['playerdata.RbSeason']"})
        },
        'playerdata.rbplayer': {
            'Meta': {'object_name': 'RbPlayer'},
            'career_rushing_attempts': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'career_rushing_yards': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dob': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'height': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'position': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'weight': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'playerdata.rbseason': {
            'Meta': {'object_name': 'RbSeason'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'player': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['playerdata.RbPlayer']"}),
            'season_rushing_attempts': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'season_rushing_yards': ('django.db.models.fields.SmallIntegerField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['playerdata']