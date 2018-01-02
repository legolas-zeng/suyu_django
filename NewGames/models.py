# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.
class new_game_plan(models.Model):
	ids = models.CharField(max_length=255,verbose_name=u"新服订单号",unique=True)
	platform = models.CharField(max_length=255, verbose_name=u"平台")
	name = models.CharField(max_length=255, verbose_name=u"区服名称")
	game = models.CharField(max_length=255)
	areas = models.CharField(max_length=16, verbose_name=u"游戏编号", default=0)
	game_id = models.CharField(max_length=255, verbose_name=u"唯一ID")
	open_date = models.DateTimeField(max_length=255,verbose_name=u"开服时间")
	apply_date = models.DateTimeField(max_length=255,verbose_name=u"申请时间")
	state = models.CharField(max_length=16,default=1)
	progress = models.CharField(verbose_name=u"安装进度", default=0, max_length=255)
	success = models.IntegerField(default=0, verbose_name=u"是否完成")
	ip = models.ForeignKey('Hosts',null=True) # 非空约束，外键
	'''
	success = 0 没有安装
	success = 1 等待安装
	success = 2 开始安装
	success = 3 完成安装 '''
	
	class Meta:
		verbose_name=u"新服详情"
		verbose_name_plural=u"新服申请"
		
class Hosts(models.Model):
	country_choices = (
		('china', u'国服'),
		('vietnam', u'越南'),
		('tmldyn', u'越南唐门'),
		('golden', u'辉耀'),
		# ('hongkong', u'港澳台'),
		('kuaiyou', u'快游'),
		('miaole', u'秒乐'),
		('xxqy', u'仙侠情缘'),
		('6kw', u'6kw'),
		('chuangxing', u'创星'),
	)
	
	app_choices = (
		('s1', 's1'),
		('s2', 's2')
	)
	
	country = models.CharField(verbose_name=u"游戏区域", choices=country_choices, default='china', max_length=50);
	app = models.CharField(verbose_name=u"中心服", choices=app_choices, default='s1', max_length=50);
	hostName = models.CharField(verbose_name=u'主机名称', max_length=200)
	hostWanIp = models.GenericIPAddressField(verbose_name=u"外网IP", unique=True)
	hostLanIp = models.GenericIPAddressField(verbose_name=u"内网IP", blank=True, null=True)
	hostDomain = models.CharField(verbose_name=u'主机域名', max_length=300, blank=True, help_text=u"主机域名为空则会读取IP")
	hostLimit = models.IntegerField(verbose_name=u"主机最大区服数", default=5)
	hostAddTime = models.DateTimeField(verbose_name=u"主机添加时间", auto_now_add=True)
	
	
	def __unicode__(self):
		return u"%s_%s %s" % (self.country, self.app, self.hostWanIp)
	
	class Meta:
		verbose_name = u'主机'
		verbose_name_plural = u'主机列表'
