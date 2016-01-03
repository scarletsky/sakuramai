#-*- coding:utf-8 -*-
from django.db import models
from datetime import datetime


class Vote2013(models.Model):
    ipaddr = models.IPAddressField(u'IP地址')
    day = models.IntegerField(u'天数')
    team_num = models.IntegerField(u'组号')
    pub_time = models.DateTimeField(u'报名日期', auto_now_add=True)

    class Meta:
        db_table = 'skm_vote'

    def __unicode__(self):
        return self.ipaddr


class Signup(models.Model):
    author = models.CharField(u'名称', max_length=32)
    contact = models.CharField(u'联系方式', max_length=64)
    remark = models.TextField(u'备注', blank=True)
    is_team = models.BooleanField(u'是否组队')
    pub_time = models.DateTimeField(u'报名日期', auto_now_add=True)
    pair_num = models.IntegerField(u'自选配对号', default=-1)
    pair_num_fixed = models.SmallIntegerField(
        u'调整配对号',
        default=-1,
        help_text=u'调整配对号,组队报名的填-1')
    team_num = models.IntegerField(u'组号', default=-1)
    year = models.SmallIntegerField(u'年份', default=datetime.now().year)

    class Meta:
        ordering = ['-year', '-id']

    def __unicode__(self):
        return self.author


class Mad(models.Model):
    title = models.CharField(u'作品名称', max_length=128)
    author = models.CharField(u'作者', max_length=32)
    source = models.CharField(u'素材', max_length=128, blank=True)
    music = models.CharField(u'音乐', max_length=128, blank=True)
    download1 = models.URLField(u'下载地址1', blank=True)
    download2 = models.URLField(u'下载地址2', blank=True)
    image = models.URLField(u'封面图', blank=True)
    online = models.TextField(u'在线地址', blank=True)
    feeling = models.TextField(u'感想', blank=True)
    team_num = models.IntegerField(u'组号', default=0)
    is_ntr = models.BooleanField(u'是否被NTR', default=False)
    year = models.SmallIntegerField(u'年份', default=datetime.now().year)

    class Meta:
        ordering = ['-year', '-id']

    def __unicode__(self):
        return self.title


class Schedule(models.Model):
    day = models.CharField(
        u'天数',
        max_length=4,
        help_text=u'填写01, 02, 15, sp1等，用于url匹配天数')
    day_id = models.SmallIntegerField(
        u'天数id',
        default=0,
        help_text=u'这个字段用于天数排序, 一般按照顺序来就好了')
    description = models.CharField(
        u'描述',
        max_length=32,
        help_text=u'填写第一日，第二日，最终日等')
    team1 = models.SmallIntegerField(
        u'组别1',
        default=-1,
        help_text=u'填写出战的组号1')
    team2 = models.SmallIntegerField(
        u'组别2',
        default=-1,
        help_text=u'填写出战的组号2')
    vote_limit_day = models.SmallIntegerField(u'投票剩下天数', default=7)
    is_display = models.BooleanField(u'是否显示', default=False)
    year = models.SmallIntegerField(u'年份', default=datetime.now().year)

    class Meta:
        ordering = ['-year', '-id']

    def __unicode__(self):
        return self.day


class VoteDetail(models.Model):
    ip_addr = models.IPAddressField(u'IP地址')
    team_num = models.IntegerField(u'组号', default=-1)
    year = models.SmallIntegerField(u'年份', default=datetime.now().year)
    vote_time = models.DateTimeField(u'投票时间', auto_now_add=True)

    class Meta:
        ordering = ['-year', '-id']

    def __unicode__(self):
        return self.ip_addr


class Team(models.Model):
    team_num = models.IntegerField(u'组号', default=-1)
    votes = models.IntegerField(u'得票数', default=0)
    year = models.SmallIntegerField(u'年份', default=datetime.now().year)

    class Meta:
        ordering = ['-year', '-votes']

    def __unicode__(self):
        return unicode(self.team_num)
