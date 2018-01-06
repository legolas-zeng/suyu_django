# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse,request,Http404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.db.models import Q
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.template import RequestContext, Context
from django.core.urlresolvers import reverse
from suyusys.views import ret_info
from suyusys.function import *
from models import *
from suyusys.models import *
from scripts.constant import *

# Create your views here.
@csrf_exempt
def newgameplan(request,template='NewGames/new_game_plan.html'):
	#updata_new_game_api()
	#temporary_1()
	hefu_count = ret_info()
	gamelist = new_game_plan.objects.filter(state=1)
	context = {
		'gamelist':gamelist,
		'hefu_count': hefu_count
	}
	return render(request,template,context)
@csrf_exempt
def new_game_progress(request,template='NewGames/new_game_progress.html'):
	return render(request,template)

@csrf_exempt
def new_game_api(request):
	if request.method == 'POST':
		new_game_list = json.loads(request.body)
		ids = new_game_list.get('ids')
		platfrom = new_game_list.get('platform')
		'''这里需要做一次判断，用于更新platform'''
		dic = {}
		for k, v in zip(ids, platfrom):
			dic.setdefault(k, []).append(v)
		print dic
		for key, value in dic.items():
			for game in value:
				country = list(PLATFORM_INFO.keys())[list(PLATFORM_INFO.values()).index(game)]
				print u"订单%s，游戏%s"%(key,country)
				'''到这一步就可以知道新服订单的所以信息
				   算出适合的安装的主机'''
				
		get_info(802,'tmld_6k')
def temporary_1():
	a = new_game('111')
	b= a.new_platform()
	print b[0]
	for c in b :
		infoss = list()
		ids = c[0]
		game = c[1]
		platform = c[2]
		print ids,game,platform
		infoss.append(platfrom_map(ids=ids,game=game,platform=platform))
		platfrom_map.objects.bulk_create(infoss)
def get_keys(d, value):
    return [k for k,v in d.items() if v == value]
# 获取到新服订单信息
def get_info(ids,country):
	info = new_game_plan.objects.get(ids=ids)
	game = info.game
	platform = info.platform
	name = info.name
	open_date = info.open_date
	country = country
	print game,platform,name,open_date,country
# 分配IP
def get_ip(game,server,name,platfrom,open_date):
	pass
	
		
		
		
		
