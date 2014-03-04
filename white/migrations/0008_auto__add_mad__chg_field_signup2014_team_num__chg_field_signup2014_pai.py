# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Mad'
        db.create_table(u'white_mad', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('author', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('source', self.gf('django.db.models.fields.CharField')(max_length=128, blank=True)),
            ('music', self.gf('django.db.models.fields.CharField')(max_length=128, blank=True)),
            ('download1', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('download2', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('image', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('online', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('feeling', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('team_num', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('is_ntr', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('year', self.gf('django.db.models.fields.SmallIntegerField')(default=2014)),
        ))
        db.send_create_signal(u'white', ['Mad'])


        # Changing field 'Signup2014.team_num'
        db.alter_column(u'white_signup2014', 'team_num', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'Signup2014.pair_num'
        db.alter_column(u'white_signup2014', 'pair_num', self.gf('django.db.models.fields.IntegerField')())

    def backwards(self, orm):
        # Deleting model 'Mad'
        db.delete_table(u'white_mad')


        # Changing field 'Signup2014.team_num'
        db.alter_column(u'white_signup2014', 'team_num', self.gf('django.db.models.fields.IntegerField')(max_length=2))

        # Changing field 'Signup2014.pair_num'
        db.alter_column(u'white_signup2014', 'pair_num', self.gf('django.db.models.fields.IntegerField')(max_length=2))

    models = {
        u'white.mad': {
            'Meta': {'object_name': 'Mad'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'download1': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'download2': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'feeling': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'is_ntr': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'music': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'online': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'source': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'team_num': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'year': ('django.db.models.fields.SmallIntegerField', [], {'default': '2014'})
        },
        u'white.signup2014': {
            'Meta': {'object_name': 'Signup2014'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'contact': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_team': ('django.db.models.fields.BooleanField', [], {}),
            'pair_num': ('django.db.models.fields.IntegerField', [], {'default': '-1'}),
            'pub_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'remark': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'team_num': ('django.db.models.fields.IntegerField', [], {'default': '-1'}),
            'year': ('django.db.models.fields.SmallIntegerField', [], {'default': '2014'})
        }
    }

    complete_apps = ['white']