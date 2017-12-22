# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,render_to_response,redirect
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse,request,Http404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.db.models import Q
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.template import RequestContext, Context
from django.core.urlresolvers import reverse
from django import forms
from suyu.models import *
from suyusys.models import *
from suyu.models import redisinfo
import json,sys
import datetime
import os
from scripts.constant import DB_INFO
import MySQLdb
from scripts import hefu_test

# Create your views here.
def newindex(request,template='newindex.html'):
	db_key = 'china_gmdb'
	db_info = DB_INFO.get(db_key)
	db = MySQLdb.connect(host=db_info['host'], user=db_info['user'], passwd=db_info['pwd'], db=db_info['dbname'],
	                     port=db_info['port'])
	cursor = db.cursor()
	cursor.execute("select count(1) from server_combine where status='1';")
	datas = cursor.fetchall()
	for a in datas:
		for hefu_count in a:
			print hefu_count
	context = {
		'hefu_count':hefu_count
	}
	print context
	return render(request,template,context)
def ret_info():
	db_key = 'china_gmdb'
	db_info = DB_INFO.get(db_key)
	db = MySQLdb.connect(host=db_info['host'], user=db_info['user'], passwd=db_info['pwd'], db=db_info['dbname'],
	                     port=db_info['port'])
	cursor = db.cursor()
	cursor.execute("select count(1) from server_combine where status='1';")
	datas = cursor.fetchall()
	for a in datas:
		for hefu_count in a:
			print hefu_count
	return hefu_count
def redis_info(request,template='suyusys/redis-info.html'):
	info_list = DbServersRedis.objects.all()
	hefu_count = ret_info()
	context = {
		'redisinfo': info_list,
		'hefu_count': hefu_count
	}
	return render(request, template, context)
def echart_redis(request,template='suyusys/echart_redis.html'):
	ip = request.GET['chart']
	hefu_count = ret_info()
	context = {
		'ip':ip,
		'hefu_count': hefu_count
	}
	return render(request,template,context)
	
def Api_echart_redis(request,template='apichartredis.html'):
	ip = request.GET['echart']
	print ip
	line_dict = {'categories': [], 'data': []}
	redis_info_list = Redisinfotest.objects.filter(hostip=ip)
	for line in redis_info_list:
		line_dict['categories'].append(line.autoTime)
		line_dict['data'].append(line.connected)
	print line_dict
	return JsonResponse(line_dict)
def globa_setting(request,template='suyusys/globa_setting.html'):
	return render(request,template)
def Notifications(request,template='suyusys/Notifications.html'):
	pass
def hefu_game(request,template='suyusys/hefu_game_plan.html'):
	hefu_count = ret_info()
	db_key = 'china_gmdb'
	db_info = DB_INFO.get(db_key)
	db = MySQLdb.connect(host=db_info['host'], user=db_info['user'], passwd=db_info['pwd'], db=db_info['dbname'],
	                     port=db_info['port'])
	cursor_now = db.cursor()
	cursor_now.execute("select id from server_combine order by id desc limit 1;")
	datas = cursor_now.fetchall()
	for datas in datas:
		for now_id in datas:
			print u"远程数据库最大ID：",now_id
	'''now_id  数据库合服ID最大值
	   now_ids sqlite数据库合服ID最大值'''
	# now_id_exit=hefuinfo.objects.filter(hefuid=now_id)
	
	now_id_ob = hefuinfo.objects.order_by("-hefuid")[0:1].get() # 逆向排序取最大ID
	now_ids = int(now_id_ob.hefuid)
	print u"本地数据库最大ID：", now_ids
	
	if int(now_id)>now_ids:
		print u"合服数据库有更新"
		for num in range(now_ids+1,int(now_id)+1):
			print num
			cursor_hefu = db.cursor()
			cursor_hefu.execute('select * from server_combine where id = %s',num)
			hefu_data = cursor_hefu.fetchall()
			hefu_info = list()
			for hefu_datas in hefu_data:
				hefuid = hefu_datas[0]
				game = hefu_datas[1]
				platform = hefu_datas[2]
				area = hefu_datas[3]
				serverid = hefu_datas[4]
				serverids = hefu_datas[5]
				apply_time = hefu_datas[6]
				status = hefu_datas[7]
				combine_time = hefu_datas[8]
				print hefuid,game,platform,area,serverid,serverids,apply_time,status,combine_time
			cursor_hefu.execute('select ip from game_servers where server=%s',serverid)
			server_ip = cursor_hefu.fetchall()
			for main_server_ip in server_ip:
				main_server_ip = main_server_ip[0]
				print u"主服IP：",main_server_ip[:-5]
				main_server_ip = main_server_ip[:-5]
			hefu_info.append(hefuinfo(hefuid=hefuid,game=game,platform=platform,area=area,server_id=serverid,server_ids=serverids,apply_time=apply_time,status=status,combine_time=combine_time,main_server_ip=main_server_ip))
			hefuinfo.objects.bulk_create(hefu_info)
		cursor_hefu.close()
	else:
		print u"合服数据库没有更新"
	status_id = hefuinfo.objects.filter(status=1).values('hefuid')
	for status_ids in status_id:
		for id in status_ids.values():
			print id
			cursor_now.execute('select status from server_combine where id=%s',id)
			status = cursor_now.fetchall()
			for statuss in status:
				for sta in statuss:
					hefuinfo.objects.filter(hefuid=id).update(status=sta) # 后台提交，更改数据库status状态
	cursor_now.close()
	db.close()
	hefu_data = hefuinfo.objects.filter(status=1)                         # 只返回status=1的订单
	context = {
		'hefu_datas':hefu_data,
		'hefu_count': hefu_count
	}
	return render(request,template,context)
@csrf_exempt
def HefuInput(request,template='suyusys/HefuInput.html'): # 提交开始合服
	if request.method == 'POST':
		hefu_list = json.loads(request.body)
		ip = hefu_list.get('ip')
		id = hefu_list.get('hefuid')
		dic = {}
		for ids in id:
			hefuinfo.objects.filter(hefuid=ids).update(success=1) # 订单状态改为正在合服
		for k, v in zip(ip, id):
			dic.setdefault(k, []).append(v)
		a = len(dic)
		i = 0
		for i in range(0, a):
			list_info = dic.items()[i]
			id_list = list_info[1]
			ip_list = list_info[0]
			print ip_list
			dc = len(id_list)
			for id_info in id_list:
				print id_info
				hefu_id = hefuinfo.objects.filter(hefuid=id_info).values('server_id')
				hefu_ids = hefuinfo.objects.filter(hefuid=id_info).values('server_ids')
				print hefu_id,hefu_ids
			'''提取区服号，调用salt模块执行'''
@csrf_exempt
def HefuProgressApi(request):  # 接收合服脚本返回的合服进度
    if request.method=='POST':
        req=json.loads(request.body)
        hostdata=list()
        print req
        pro = req.get('pro')
        proed = str(pro * 25)
        print proed
        hefu_id = req.get('hefu_id')
        print hefu_id
        T = hefuinfo.objects.get(hefuid=hefu_id)
        T.progress = proed
        T.save()
    return HttpResponse('1')
@csrf_exempt
def HefuProgress(request,template='suyusys/HefuProgress.html'):
	hefu_list = hefuinfo.objects.filter(success__gte=1)
	hefu_count = ret_info()
	context = {
		'hefu_list': hefu_list,
		'hefu_count':hefu_count
	}
	return render(request, template, context)
@csrf_exempt
def hefu_log_api(request): # 发送合服详细日志的
	if request.method == 'POST' :
		req = json.loads(request.body)
		hostdata = list()
		print req
@csrf_exempt
def HefuProgressSearch(request):
	if request.method == 'POST': # 发送合服进度给web
		fileid_list = json.loads(request.body)
		print fileid_list
		hefu_list = list(hefuinfo.objects.filter(success__gte = 0).values('hefuid','progress'))
		print hefu_list
		#data = serializers.serialize("json",hefuinfo.objects.filter(success__gte = 0))
		#data = serializers.serialize("json", hefuinfo.objects.filter(success__gte=0).values('hefuid','progress'))
		#print data
		#return HttpResponse(hefu_list)
		return HttpResponse(json.dumps(hefu_list))
		
def file_upload(request,template='suyusys/File_upload.html'):
	return render(request,template)
