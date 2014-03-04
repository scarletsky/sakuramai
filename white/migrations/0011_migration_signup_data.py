# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

class Migration(DataMigration):

    def forwards(self, orm):
        authors = orm.Signup2013.objects.all()
        for author in authors:
            pair_num = author.pair_num if author.pair_num else -1
            team_num = author.team_num if author.team_num else -1

            newAuthor = orm.Signup2014(
                author=author.author,
                contact=author.contact,
                remark=author.remark,
                is_team=author.is_team,
                pub_time=author.pub_time,
                pair_num=pair_num,
                pair_num_fixed=pair_num,
                team_num=team_num,
                year=2013)
            newAuthor.save()


    def backwards(self, orm):
        "Write your backwards methods here."

    models = {
        u'white.day2013': {
            'Meta': {'ordering': "['id']", 'object_name': 'Day2013', 'db_table': "'skm_day'"},
            'display': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'url_index': ('django.db.models.fields.CharField', [], {'max_length': '4'})
        },
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
        u'white.mad2013': {
            'Meta': {'ordering': "['-day']", 'object_name': 'Mad2013', 'db_table': "'skm_mad'"},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'day': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '3', 'blank': 'True'}),
            'download1': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'download2': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'feeling': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'is_display': ('django.db.models.fields.BooleanField', [], {}),
            'is_ntr': ('django.db.models.fields.BooleanField', [], {}),
            'limit_days': ('django.db.models.fields.IntegerField', [], {'default': '7'}),
            'music': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'online': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'source': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'team_num': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '3', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'votes': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'white.schedule': {
            'Meta': {'object_name': 'Schedule'},
            'day': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'day_id': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_display': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'team1': ('django.db.models.fields.SmallIntegerField', [], {'default': '-1'}),
            'team2': ('django.db.models.fields.SmallIntegerField', [], {'default': '-1'}),
            'vote_limit_day': ('django.db.models.fields.SmallIntegerField', [], {'default': '7'}),
            'year': ('django.db.models.fields.SmallIntegerField', [], {'default': '2014'})
        },
        u'white.signup2013': {
            'Meta': {'object_name': 'Signup2013', 'db_table': "'skm_signup'"},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'contact': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_team': ('django.db.models.fields.BooleanField', [], {}),
            'pair_num': ('django.db.models.fields.IntegerField', [], {'max_length': '1', 'blank': 'True'}),
            'pub_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'remark': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'team_num': ('django.db.models.fields.IntegerField', [], {'max_length': '2', 'blank': 'True'})
        },
        u'white.signup2014': {
            'Meta': {'object_name': 'Signup2014'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'contact': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_team': ('django.db.models.fields.BooleanField', [], {}),
            'pair_num': ('django.db.models.fields.IntegerField', [], {'default': '-1'}),
            'pair_num_fixed': ('django.db.models.fields.SmallIntegerField', [], {'default': '-1'}),
            'pub_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'remark': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'team_num': ('django.db.models.fields.IntegerField', [], {'default': '-1'}),
            'year': ('django.db.models.fields.SmallIntegerField', [], {'default': '2014'})
        },
        u'white.vote2013': {
            'Meta': {'object_name': 'Vote2013', 'db_table': "'skm_vote'"},
            'day': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ipaddr': ('django.db.models.fields.IPAddressField', [], {'max_length': '15'}),
            'pub_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'team_num': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['white']
    symmetrical = True
