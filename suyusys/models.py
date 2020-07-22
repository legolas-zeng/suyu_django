# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from NewGames.models import *

# Create your models here.
class DbServersRedis(models.Model):
	Status = (
		('Ture', 'ON'),
		('False', 'OFF'),
	)
	Status_2 = (
		('main', 'main'),
		('subordinate', 'subordinate'),
	)
	hostip = models.GenericIPAddressField(max_length=255,default='0.0.0.0',verbose_name=u"主机IP")
	port = models.CharField(max_length=10,verbose_name=u"端口")
	monitor = models.CharField(choices=Status, null=True,default='Ture',verbose_name=u"是否开启监控",max_length=30)
	tags = models.CharField(max_length=50, blank=True, null=True)
	role = models.CharField(choices=Status_2,max_length=30,default='subordinate',verbose_name=u"角色")
	alive = models.BooleanField(default=False,verbose_name=u"是否在线")
	connected = models.CharField(max_length=255, default=0,verbose_name=u"连接数")
	def __unicode__(self):
		return self.hostip
	class Meta:
		verbose_name = u'监控主机'
		verbose_name_plural = u'redis监控机组'
class Redisinfotest(models.Model):
	hostip = models.GenericIPAddressField(max_length=255, default='0.0.0.0')
	role = models.CharField(max_length=255)
	alive = models.BooleanField(default=False)
	connected = models.CharField(max_length=255, default=0)
	autoTime = models.DateTimeField(verbose_name=u"上报时间", auto_now_add=True)
class hefuinfo(models.Model):
	hefuid = models.CharField(unique=True,verbose_name=u"合服订单号",max_length=255)
	ip = models.GenericIPAddressField(verbose_name=u"主服ip",max_length=255,default='0.0.0.0')
	game = models.CharField(verbose_name=u"游戏版本",max_length=255,default='golden')
	platform = models.CharField(max_length=255,verbose_name=u"平台")
	area = models.CharField(verbose_name=u"区服号",max_length=255)
	server_id = models.CharField(verbose_name=u"主服ID",max_length=255)
	server_ids = models.CharField(verbose_name=u"合并服ID",max_length=255)
	apply_time = models.DateTimeField(verbose_name=u"申请时间",max_length=255)
	status = models.CharField(verbose_name=u"订单状态",max_length=255)
	combine_time = models.DateTimeField(verbose_name=u"合服时间",max_length=255)
	progress = models.CharField(verbose_name=u"合服进度",default=0,max_length=255)
	success = models.IntegerField(default=0,verbose_name=u"是否完成")
	main_server_ip = models.GenericIPAddressField(max_length=255,default='0.0.0.0')
	'''
	success = 0 没有合服
	success = 1 等待合服
	success = 2 开始完成
	success = 3 完成合服 '''
	class Meta:
		verbose_name = u'合服列表'
		verbose_name_plural = u'合服详情'
class server(models.Model):
	platform = models.CharField(max_length=255, verbose_name=u"平台")
	area = models.CharField(max_length=16,verbose_name=u"游戏编号",default=0)
	app = models.CharField(max_length=16,verbose_name=u"中心服")
	app_id = models.CharField(max_length=255,verbose_name=u"游戏类")
	server = models.CharField(max_length=255,verbose_name=u"唯一ID")
	merge = models.CharField(max_length=255,verbose_name=u"合并区服")
	name = models.CharField(max_length=255,verbose_name=u"区服名称")
	game = models.CharField(max_length=255)
	show = models.CharField(max_length=16,verbose_name=u"显示号")
	status = models.CharField(max_length=16)
	offtime = models.DateTimeField(max_length=255,verbose_name=u"停服时间")
	sertime = models.DateTimeField(max_length=255,verbose_name=u"开服时间")
	ip = models.GenericIPAddressField(max_length=255,verbose_name=u"IP")
	white = models.CharField(max_length=16,verbose_name=u"白名单")
	is_open = models.BooleanField(max_length=2,verbose_name=u"是否开服")
	add_time = models.CharField(max_length=255,verbose_name=u"申请时间")
	class Meta:
		verbose_name = u'游戏列表'
		verbose_name_plural = u'游戏详情'
class Version(models.Model):
	versionid = models.CharField(max_length=255,verbose_name=u"版本号")
	updatatime = models.DateTimeField(verbose_name=u"更新时间",auto_now_add=True)
	server = models.ForeignKey('server')
	# updatazone = models.CharField(verbose_name=u"更新范围",max_length=255)
	# platform = models.CharField(max_length=255, verbose_name=u"平台")
	
	