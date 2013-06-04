#-*- coding:utf-8 -*-

from django.db import models


class Signup(models.Model):
	author = models.CharField(u'名称', max_length=32)
	contact = models.CharField(u'联系方式', max_length=64)
	remark = models.TextField(u'备注', blank=True)
	pair_num = models.IntegerField(u'配对号', max_length=1, blank=True)
	team_num = models.IntegerField(u'组号', max_length=2, blank=True)
	is_team = models.BooleanField(u'是否组队')
	pub_time = models.DateTimeField(u'报名日期', auto_now_add=True)

	def __unicode__(self):
		return self.author




class Staff(models.Model):
	name = models.CharField(u'成员名称', max_length=32)
	join_in = models.CharField(u'加入时间', max_length=16, blank=True)
	remark = models.TextField(u'备注', blank=True)
	is_active = models.BooleanField(u'是否活动')

	def __unicode__(self):
		return self.name


class Day(models.Model):
	url_index = models.CharField(u'day', max_length=4, help_text="用于/2013/xx，填数字(01, 02等)， 小甜点填sp")
	display = models.CharField(u'显示', max_length=8, help_text="填第一日, 最终日等")

	class Meta:
		ordering = ['id']

	def __unicode__(self):
		return self.display


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
	day = models.IntegerField(u'天数', max_length=3, blank=True, help_text="小甜点填99", default=0)
	team_num = models.IntegerField(u'组号', max_length=3, blank=True, default=0)
	votes = models.IntegerField(u'得票数', default=0)
	limit_days = models.IntegerField(u'投票剩下日期', default=7)
	is_ntr = models.BooleanField(u'是否被NTR')
	is_display = models.BooleanField(u'是否显示')

	class Meta:
		ordering = ['-day']


	def __unicode__(self):
		return self.title


class Vote(models.Model):
	ipaddr = models.IPAddressField(u'IP地址')
	day = models.IntegerField(u'天数')
	team_num = models.IntegerField(u'组号')
	pub_time = models.DateTimeField(u'报名日期', auto_now_add=True)

	def __unicode__(self):
		return self.ipaddr


