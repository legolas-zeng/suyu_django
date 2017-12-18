# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.shortcuts import render,render_to_response,redirect
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse,request,Http404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.template import RequestContext, Context
from django.core.urlresolvers import reverse
from django import forms
from suyu.models import *
from suyusys.models import *
from suyu.models import redisinfo
import json
import datetime
import os
from scripts import test,hefu_test
from scripts.constant import DB_INFO
import MySQLdb

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
	context = {
		'hefu_count': hefu_count
	}
	return render(request,template,context)
@csrf_exempt
def hefu_input(request,template='suyusys/hefu_input.html'):
	if request.method == 'POST':
		hefu_list = json.loads(request.body)
		print hefu_list
		'''获取到合服订单ID后这里写合服功能代码'''
		'''额外传合服订单ID给合服脚本'''
@csrf_exempt
def hefu_progress(request,template='suyusys/hefu_progress.html'):
	if request.method == 'POST':
		req = json.loads(request.body)
		pro = req.get('pro')
		status = req.get('status')
		hefu_id = req.get('hefu_id')
		print pro, status, hefu_id
		results = test(hostip, modelname)
		return HttpResponse(json.dumps(results))
			
	return render(request,template)
def file_upload(request,template='suyusys/File_upload.html'):
	return render(request,template)
