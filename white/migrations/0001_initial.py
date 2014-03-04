# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Signup2014'
        db.create_table(u'white_signup2014', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('author', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('contact', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('remark', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('pair_num', self.gf('django.db.models.fields.CharField')(max_length=1, blank=True)),
            ('team_num', self.gf('django.db.models.fields.CharField')(max_length=2, blank=True)),
            ('is_team', self.gf('django.db.models.fields.BooleanField')()),
            ('pub_time', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'white', ['Signup2014'])


    def backwards(self, orm):
        # Deleting model 'Signup2014'
        db.delete_table(u'white_signup2014')


    models = {
        u'white.signup2014': {
            'Meta': {'object_name': 'Signup2014'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'contact': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_team': ('django.db.models.fields.BooleanField', [], {}),
            'pair_num': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'pub_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'remark': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'team_num': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'})
        }
    }

    complete_apps = ['white']