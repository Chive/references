# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Reference'
        db.create_table(u'references_reference', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('donor_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('donor_logo', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('donor_detail_img', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('donor_title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('reference_text', self.gf('django.db.models.fields.TextField')()),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'references', ['Reference'])


    def backwards(self, orm):
        # Deleting model 'Reference'
        db.delete_table(u'references_reference')


    models = {
        u'references.reference': {
            'Meta': {'object_name': 'Reference'},
            'donor_detail_img': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'donor_logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'donor_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'donor_title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {}),
            'reference_text': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['references']