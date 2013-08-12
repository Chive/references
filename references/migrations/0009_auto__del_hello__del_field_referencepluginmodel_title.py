# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Hello'
        db.delete_table(u'cmsplugin_hello')

        # Deleting field 'ReferencePluginModel.title'
        db.delete_column(u'cmsplugin_referencepluginmodel', 'title')

        # Adding M2M table for field references on 'ReferencePluginModel'
        db.create_table(u'references_referencepluginmodel_references', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('referencepluginmodel', models.ForeignKey(orm[u'references.referencepluginmodel'], null=False)),
            ('reference', models.ForeignKey(orm[u'references.reference'], null=False))
        ))
        db.create_unique(u'references_referencepluginmodel_references', ['referencepluginmodel_id', 'reference_id'])


    def backwards(self, orm):
        # Adding model 'Hello'
        db.create_table(u'cmsplugin_hello', (
            ('guest_name', self.gf('django.db.models.fields.CharField')(default='Guest', max_length=50)),
            (u'cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'references', ['Hello'])

        # Adding field 'ReferencePluginModel.title'
        db.add_column(u'cmsplugin_referencepluginmodel', 'title',
                      self.gf('django.db.models.fields.CharField')(default='nada', max_length=50),
                      keep_default=False)

        # Removing M2M table for field references on 'ReferencePluginModel'
        db.delete_table('references_referencepluginmodel_references')


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
            'donor_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'donor_title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {}),
            'reference_text': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'})
        },
        u'references.referencepluginmodel': {
            'Meta': {'object_name': 'ReferencePluginModel', 'db_table': "u'cmsplugin_referencepluginmodel'", '_ormbases': ['cms.CMSPlugin']},
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'references': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['references.Reference']", 'symmetrical': 'False'})
        }
    }

    complete_apps = ['references']