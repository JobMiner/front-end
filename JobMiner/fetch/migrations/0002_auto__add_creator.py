# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Creator'
        db.create_table(u'fetch_creator', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=31)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=31)),
        ))
        db.send_create_signal(u'fetch', ['Creator'])


    def backwards(self, orm):
        # Deleting model 'Creator'
        db.delete_table(u'fetch_creator')


    models = {
        u'fetch.creator': {
            'Meta': {'object_name': 'Creator'},
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '31'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '31'})
        }
    }

    complete_apps = ['fetch']