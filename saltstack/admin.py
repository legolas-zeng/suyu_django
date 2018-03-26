# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from saltstack.models import *

# Register your models here.
class ZoneModulesAdmin(admin.ModelAdmin):
    list_display = ['moduleCnName', 'moduleName', 'moduleIsUseId', 'moduleArgvCount', 'moduleArgv1', 'moduleArgv2',
                    'moduleArgv3']
    list_display_links = ['moduleCnName']
    ordering = ['moduleCnName']
    search_fields = ['moduleIsUseId']
    
class SaltServerAdmin(admin.ModelAdmin):
    list_display = ['url','username','password','role']
    list_filter=['role']
class MinionsAdmin(admin.ModelAdmin):
    list_display = ['minion','saltserver','status','create_date']
    list_filter=['status','saltserver']
class MinionGroupAdmin(admin.ModelAdmin):
    list_display = ['groupname']
    list_filter=['minions']
class SaltJobsModels(admin.ModelAdmin):
    list_display = ('jid','args','function','target','startTime','saltserver','user')
    search_fields = ('function','jid')
class CmdRunLogModels(admin.ModelAdmin):
    list_display = ('user','time','target','cmd','total','runsuccess','runerror')
    search_fields = ('user','cmd')

admin.site.register(ZoneModules, ZoneModulesAdmin)
admin.site.register(saltserver,SaltServerAdmin)
admin.site.register(Minions,MinionsAdmin)
admin.site.register(MinionGroup,MinionGroupAdmin)
admin.site.register(SaltJobs,SaltJobsModels)
admin.site.register(CmdRunLog,CmdRunLogModels)
admin.site.register(Modules)