# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from suyu.models import Host,IDC,runmodel,uploadfile


class HostAdmin(admin.ModelAdmin):
    list_display = ['hostname','ip','osversion','memory','disk','model_name','cpu_core','host_status','host_IDC']
    list_display_links=['ip']
    ordering=['hostname']
    list_filter=['host_status']
class uploadAdmin(admin.ModelAdmin):
    list_display=['filetitle','filepath','fileexit','uploadtime','filesize']
    list_display_lisks=['filetitle']
    search_fields = ['filetitle', 'uploadtime']
    list_filter = ['filepath','fileexit']
class runmodelAdmin(admin.ModelAdmin):
    list_display = ['model','modelname','modelid']
admin.site.register(IDC) 
admin.site.register(Host,HostAdmin)
admin.site.register(runmodel,runmodelAdmin)
admin.site.register(uploadfile,uploadAdmin)
