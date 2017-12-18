# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django import forms
from datetime import datetime

class IDC(models.Model):
    idc_name = models.CharField(verbose_name=u"机房",max_length=100)
    idc_laber= models.CharField(verbose_name=u'标签',max_length=100)
    def __unicode__(self):
        return "%s"%(self.idc_name)
    class Meta:
        verbose_name=u'机房'
        verbose_name_plural=u'IDC'

class Host(models.Model):
    hostStatus_chices=(
    (1,u'在用'),
    (2,u'空闲'),
    (3,u'停用'),
    )
    hostname = models.CharField(verbose_name=u"主机名称",default='server',max_length=50,unique=True,help_text=u"格式为server+平台+编号")
    host_IDC = models.ForeignKey(IDC,default=1)
    ip = models.GenericIPAddressField(verbose_name=u"主机IP",unique=True)
    osversion = models.CharField(verbose_name=u"操作系统",default='Linux',max_length=50)
    memory = models.CharField(verbose_name=u"内存",default='2G',max_length=50)
    disk = models.CharField(verbose_name=u"硬盘",max_length=50)
    model_name = models.CharField(verbose_name=u"型号",blank=True,max_length=50)
    cpu_core = models.CharField(verbose_name=u"cpu核数",max_length=50)
    host_status=models.IntegerField(verbose_name=u'主机状态',choices=hostStatus_chices,default=1)
    test=models.CharField(verbose_name=u"test",max_length=50)
    class Meta:
        verbose_name=u'主机'  
        verbose_name_plural=u'主机列表'  
class autohost(models.Model):
    autohostname=models.CharField(verbose_name=u"主机名", default=0,max_length=100)
    autoip=models.GenericIPAddressField(verbose_name=u"IP", default=0)
    #autoosversion=models.IntegerField(verbose_name=u"系统版本", default=0)
    #automemory=models.IntegerField(verbose_name=u"内存", default=0)
    autodisk=models.CharField(verbose_name=u"硬盘", default=0,max_length=100)
    autocpucore=models.CharField(verbose_name=u"cpu使用率", default=0,max_length=100)
    autoTime = models.DateTimeField(verbose_name=u"上报时间", auto_now_add=True)
    mencached = models.CharField(verbose_name=u"页面缓存", default=0, max_length=100)
    menbuffer = models.CharField(verbose_name=u"高速缓存", default=0, max_length=100)
    menswap = models.CharField(verbose_name=u"交换分区", default=0, max_length=100)
    def __unicode__(self):
        return "%s" % self.autohostnames

class runmodel(models.Model):
    model = models.CharField(verbose_name=u"标签",max_length=100)
    modelid = models.CharField(verbose_name=u"模块ID",max_length=10,default=0)
    modelname= models.CharField(verbose_name=u'模块名',max_length=100)
    def __unicode__(self):
        return "%s(%s)"%(self.model,self.modelname)
    class Meta:
        verbose_name=u'标签'
        verbose_name_plural=u'模块名'
class uploadfile(models.Model):
    filepath_chices = (
        (1, 'F:\django_test\media'),
        (2, '00000'),
    )
    filetitle = models.CharField(verbose_name=u"文件名",default=0,max_length=255)
    filepath = models.CharField(verbose_name=u"文件目录",max_length=255,default=2)
    fileexit = models.BooleanField(verbose_name=u"是否存在", default=True)
    uploadtime = models.DateTimeField(verbose_name=u"上传时间",auto_now_add=True)
    filesize = models.CharField(verbose_name=u"文件大小",default=0,max_length=255)
    def __unicode__(self):
        return self.filetitle
    class Meta:
        verbose_name=u'文件名'
        verbose_name_plural=u'上传文件'
class redisinfo(models.Model):
    hostip = models.GenericIPAddressField(max_length=255,default='0.0.0.0')
    role = models.CharField(max_length=255)
    alive = models.BooleanField(default=False)
    connected = models.CharField(max_length=255, default=0)
    redisTime = models.DateTimeField(verbose_name=u"上报时间", default=datetime.now)
    
    