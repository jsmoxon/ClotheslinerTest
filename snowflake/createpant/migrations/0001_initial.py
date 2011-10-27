# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'UserPant'
        db.create_table('createpant_userpant', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('designer', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('style', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('label_waist', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('label_inseam', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('waist', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('inseam', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('front_rise', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('back_rise', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('cuff', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('thigh', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('knee', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('hips', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('outseam', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
        ))
        db.send_create_signal('createpant', ['UserPant'])


    def backwards(self, orm):
        
        # Deleting model 'UserPant'
        db.delete_table('createpant_userpant')


    models = {
        'createpant.userpant': {
            'Meta': {'object_name': 'UserPant'},
            'back_rise': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'cuff': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'designer': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'front_rise': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'hips': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inseam': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'knee': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'label_inseam': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'label_waist': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'outseam': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'style': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'thigh': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'waist': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['createpant']
