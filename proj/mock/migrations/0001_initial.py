# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Pictures'
        db.create_table(u'mock_pictures', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('pic', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True)),
        ))
        db.send_create_signal(u'mock', ['Pictures'])

        # Adding model 'Audio'
        db.create_table(u'mock_audio', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('audio', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True)),
        ))
        db.send_create_signal(u'mock', ['Audio'])

        # Adding model 'Feed'
        db.create_table(u'mock_feed', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('feed', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True)),
        ))
        db.send_create_signal(u'mock', ['Feed'])


    def backwards(self, orm):
        # Deleting model 'Pictures'
        db.delete_table(u'mock_pictures')

        # Deleting model 'Audio'
        db.delete_table(u'mock_audio')

        # Deleting model 'Feed'
        db.delete_table(u'mock_feed')


    models = {
        u'mock.audio': {
            'Meta': {'object_name': 'Audio'},
            'audio': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'mock.feed': {
            'Meta': {'object_name': 'Feed'},
            'feed': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'mock.pictures': {
            'Meta': {'object_name': 'Pictures'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pic': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['mock']