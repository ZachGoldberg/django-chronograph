# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Job'
        db.create_table('chronograph_job', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('frequency', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('params', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('command', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('args', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('disabled', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('next_run', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('last_run', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('is_running', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('chronograph', ['Job'])

        # Adding model 'Log'
        db.create_table('chronograph_log', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('job', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['chronograph.Job'])),
            ('run_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('stdout', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('stderr', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('chronograph', ['Log'])

    def backwards(self, orm):
        
        # Deleting model 'Job'
        db.delete_table('chronograph_job')

        # Deleting model 'Log'
        db.delete_table('chronograph_log')

    models = {
        'chronograph.job': {
            'Meta': {'ordering': "('disabled', 'next_run')", 'object_name': 'Job'},
            'args': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'command': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'disabled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'frequency': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_running': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_run': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'next_run': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'params': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        'chronograph.log': {
            'Meta': {'ordering': "('-run_date',)", 'object_name': 'Log'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'job': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['chronograph.Job']"}),
            'run_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'stderr': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'stdout': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        }
    }

    complete_apps = ['chronograph']
