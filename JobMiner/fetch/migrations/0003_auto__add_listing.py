# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Listing'
        db.create_table(u'fetch_listing', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('job_id', self.gf('django.db.models.fields.CharField')(max_length=127)),
            ('employer', self.gf('django.db.models.fields.CharField')(max_length=127)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=63)),
            ('openings', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'fetch', ['Listing'])


    def backwards(self, orm):
        # Deleting model 'Listing'
        db.delete_table(u'fetch_listing')


    models = {
        u'fetch.creator': {
            'Meta': {'ordering': "('id', 'first_name')", 'object_name': 'Creator'},
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '31'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '31'})
        },
        u'fetch.listing': {
            'Meta': {'object_name': 'Listing'},
            'employer': ('django.db.models.fields.CharField', [], {'max_length': '127'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'job_id': ('django.db.models.fields.CharField', [], {'max_length': '127'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '63'}),
            'openings': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['fetch']