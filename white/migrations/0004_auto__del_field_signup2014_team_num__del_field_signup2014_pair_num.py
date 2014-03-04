# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Signup2014.team_num'
        db.delete_column(u'white_signup2014', 'team_num')

        # Deleting field 'Signup2014.pair_num'
        db.delete_column(u'white_signup2014', 'pair_num')


    def backwards(self, orm):
        # Adding field 'Signup2014.team_num'
        db.add_column(u'white_signup2014', 'team_num',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=2, blank=True),
                      keep_default=False)

        # Adding field 'Signup2014.pair_num'
        db.add_column(u'white_signup2014', 'pair_num',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=1, blank=True),
                      keep_default=False)


    models = {
        u'white.signup2014': {
            'Meta': {'object_name': 'Signup2014'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'contact': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_team': ('django.db.models.fields.BooleanField', [], {}),
            'pair_num_fix': ('django.db.models.fields.IntegerField', [], {'default': '-1', 'max_length': '2'}),
            'pub_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'remark': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'team_num_fix': ('django.db.models.fields.IntegerField', [], {'default': '-1', 'max_length': '2'})
        }
    }

    complete_apps = ['white']