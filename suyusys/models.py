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