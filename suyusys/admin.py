# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from suyusys.models import *

# Register your models here.
class DbServersRedisAdmin(admin.ModelAdmin):
	list_display = ['hostip','port','monitor','role','alive','connected']
	list_display_links = ['hostip']
class hefuinfoAdmin(admin.ModelAdmin):
	list_display = ['hefuid','platform','area','server_id','server_ids','status','combine_time','success']

admin.site.register(DbServersRedis,DbServersRedisAdmin)
admin.site.register(hefuinfo,hefuinfoAdmin)