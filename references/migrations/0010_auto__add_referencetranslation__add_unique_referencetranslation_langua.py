# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ReferenceTranslation'
        db.create_table(u'references_reference_translation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('donor_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('donor_title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('reference_text', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cms.Placeholder'], null=True)),
            ('language_code', self.gf('django.db.models.fields.CharField')(max_length=15, db_index=True)),
            ('master', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', null=True, to=orm['references.Reference'])),
        ))
        db.send_create_signal(u'references', ['ReferenceTranslation'])

        # Adding unique constraint on 'ReferenceTranslation', fields ['language_code', 'master']
        db.create_unique(u'references_reference_translation', ['language_code', 'master_id'])

        # Deleting field 'Reference.donor_title'
        db.delete_column(u'references_reference', 'donor_title')

        # Deleting field 'Reference.reference_text'
        db.delete_column(u'references_reference', 'reference_text_id')

        # Deleting field 'Reference.donor_name'
        db.delete_column(u'references_reference', 'donor_name')


    def backwards(self, orm):
        # Removing unique constraint on 'ReferenceTranslation', fields ['language_code', 'master']
        db.delete_unique(u'references_reference_translation', ['language_code', 'master_id'])

        # Deleting model 'ReferenceTranslation'
        db.delete_table(u'references_reference_translation')

        # Adding field 'Reference.donor_title'
        db.add_column(u'references_reference', 'donor_title',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=200),
                      keep_default=False)

        # Adding field 'Reference.reference_text'
        db.add_column(u'references_reference', 'reference_text',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cms.Placeholder'], null=True),
                      keep_default=False)

        # Adding field 'Reference.donor_name'
        db.add_column(u'references_reference', 'donor_name',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=200),
                      keep_default=False)


    models = {
        'cms.cmsplugin': {
            'Meta': {'object_name': 'CMSPlugin'},
            'changed_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.CMSPlugin']", 'null': 'True', 'blank': 'True'}),
            'placeholder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'}),
            'plugin_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
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
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'references.referencepluginmodel': {
            'Meta': {'object_name': 'ReferencePluginModel', 'db_table': "u'cmsplugin_referencepluginmodel'", '_ormbases': ['cms.CMSPlugin']},
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'references': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['references.Reference']", 'symmetrical': 'False'})
        },
        u'references.referencetranslation': {
            'Meta': {'unique_together': "[('language_code', 'master')]", 'object_name': 'ReferenceTranslation', 'db_table': "u'references_reference_translation'"},
            'donor_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'donor_title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'null': 'True', 'to': u"orm['references.Reference']"}),
            'reference_text': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'})
        }
    }

    complete_apps = ['references']