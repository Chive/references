# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Renaming column for 'Reference.reference_text' to match new field type.
        db.rename_column(u'references_reference', 'reference_text', 'reference_text_id')
        # Changing field 'Reference.reference_text'
        db.alter_column(u'references_reference', 'reference_text_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cms.Placeholder'], null=True))
        # Adding index on 'Reference', fields ['reference_text']
        db.create_index(u'references_reference', ['reference_text_id'])


    def backwards(self, orm):
        # Removing index on 'Reference', fields ['reference_text']
        db.delete_index(u'references_reference', ['reference_text_id'])


        # Renaming column for 'Reference.reference_text' to match new field type.
        db.rename_column(u'references_reference', 'reference_text_id', 'reference_text')
        # Changing field 'Reference.reference_text'
        db.alter_column(u'references_reference', 'reference_text', self.gf('django.db.models.fields.TextField')(default=1))

    models = {
        'cms.placeholder': {
            'Meta': {'object_name': 'Placeholder'},
            'default_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'})
        },
        u'references.reference': {
            'Meta': {'object_name': 'Reference'},
            'donor_detail_img': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'donor_logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'donor_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'donor_title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {}),
            'reference_text': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'})
        }
    }

    complete_apps = ['references']