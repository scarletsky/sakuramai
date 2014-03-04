# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

class Migration(DataMigration):

    def forwards(self, orm):
        "Write your forwards methods here."
        users = orm.Signup2014.objects.all()
        for user in users:
            if user.pair_num:
                user.pair_num_fix = user.pair_num
            if user.team_num:
                user.team_num_fix = user.team_num
            user.save()

    def backwards(self, orm):
        "Write your backwards methods here."
        users = orm.Signup2014.objects.all()
        for user in users:
            user.pair_num_fix = -1
            user.team_num_fix = -1
            user.save()

    models = {
        u'white.signup2014': {
            'Meta': {'object_name': 'Signup2014'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'contact': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_team': ('django.db.models.fields.BooleanField', [], {}),
            'pair_num': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'pair_num_fix': ('django.db.models.fields.IntegerField', [], {'default': '-1', 'max_length': '2'}),
            'pub_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'remark': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'team_num': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'team_num_fix': ('django.db.models.fields.IntegerField', [], {'default': '-1', 'max_length': '2'})
        }
    }

    complete_apps = ['white']
    symmetrical = True
