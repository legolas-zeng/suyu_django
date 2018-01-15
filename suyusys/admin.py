# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from suyusys.models import *
from NewGames.models import *

# Register your models here.
class DbServersRedisAdmin(admin.ModelAdmin):
	list_display = ['hostip','port','monitor','role','alive','connected']
	list_display_links = ['hostip']
class hefuinfoAdmin(admin.ModelAdmin):
	list_display = ['hefuid','platform','area','server_id','server_ids','status','combine_time','success','progress','main_server_ip']
	
class serverAdmin(admin.ModelAdmin):
	list_display = ['server','name','platform','status','area']
	
class newgameAdmin(admin.ModelAdmin):
	list_display = ['ids','areas','game_id','progress','success','state','name']
	
class HostsAdmin(admin.ModelAdmin):
	list_display = ['hostWanIp','hostLanIp','country','hostLimit','hostDomain','hostAddTime','hostName','app']
	list_display_links = ['country','app']
class platform_mapAdmin(admin.ModelAdmin):
	list_display = ['ids','game','platform']
	
admin.site.register(Hosts,HostsAdmin)
admin.site.register(DbServersRedis,DbServersRedisAdmin)
admin.site.register(hefuinfo,hefuinfoAdmin)
admin.site.register(server,serverAdmin)
admin.site.register(new_game_plan,newgameAdmin)
admin.site.register(platform_map,platform_mapAdmin)