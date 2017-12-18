# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.
class DbServersRedis(models.Model):
	Status = (
		('Ture', 'ON'),
		('False', 'OFF'),
	)
	Status_2 = (
		('master', 'master'),
		('slave', 'slave'),
	)
	hostip = models.GenericIPAddressField(max_length=255,default='0.0.0.0',verbose_name=u"主机IP")
	port = models.CharField(max_length=10,verbose_name=u"端口")
	monitor = models.CharField(choices=Status, null=True,default='Ture',verbose_name=u"是否开启监控",max_length=30)
	tags = models.CharField(max_length=50, blank=True, null=True)
	role = models.CharField(choices=Status_2,max_length=30,default='slave',verbose_name=u"角色")
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
	game = models.CharField(verbose_name=u"游戏版本",max_length=255,default='golden')
	platform = models.CharField(max_length=255,verbose_name=u"平台")
	area = models.CharField(verbose_name=u"区服号",max_length=255)
	server_id = models.CharField(verbose_name=u"主服ID",max_length=255)
	server_ids = models.CharField(verbose_name=u"合并服ID",max_length=255)
	apply_time = models.DateTimeField(verbose_name=u"申请时间",max_length=255)
	status = models.CharField(verbose_name=u"订单状态",max_length=255)
	combine_time = models.DateTimeField(verbose_name=u"合服时间",max_length=255)
	progress = models.CharField(verbose_name=u"合服进度",default=0,max_length=255)
	success = models.BooleanField(default=False,verbose_name=u"是否完成")
	class Meta:
		verbose_name = u'合服列表'
		verbose_name_plural = u'合服详情'