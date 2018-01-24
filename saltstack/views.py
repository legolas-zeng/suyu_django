# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,render_to_response,redirect
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse,request,Http404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.template import RequestContext, Context
from django.core.urlresolvers import reverse
from suyu.models import *
from saltstack.models import *
from suyusys.models import *
import json,datetime,os
from scripts.salt_run import test
from suyusys import views as sviews

# Create your views here.

def runzonemodules(request,template='saltstack/runzonemodules.html'):
	platform = 'tmld_6Kwan'
	server_list = server.objects.filter(platform=platform)
	
	for serverinfo in server_list:
		print serverinfo
	modules = ZoneModules.objects.all()
	context = {
		"sever_list":server_list,
		"modules":modules,
	}
	return render(request,template,context)
@csrf_exempt
def command_page(request,template='command_page.html'):
	idc_list = IDC.objects.all()
	host_list = Host.objects.all()
	model_list = runmodel.objects.all()
	context = {
		'idc_list': idc_list,
		'host_list': host_list,
		'model_list': model_list,
	}
	return render(request, template,context)
@csrf_exempt
def command_run(request,template='command_run.html'):
	if request.method == 'POST':
		info_list = json.loads(request.body)
		print info_list
		for key, value in info_list.items():
			if key == 'hostip':
				hostip = value
			if key == 'modelid':
				modelid = value
		print modelid,hostip
		model = runmodel.objects.filter(modelid=modelid).values()
		if not model:
			print u"模块不存在"
		else:
			for model_info in model:
				modelname = model_info['model']
				print modelname
		for hostip in hostip:
			host = Host.objects.filter(ip=hostip).values()
			if not host:
				print u"主机不存在"
			else:
				print 1
			results = test(hostip,modelname)
			return HttpResponse(json.dumps(results))

def saltmodule(request,template='saltstack/saltmodule_deploy.html'):
	usersession = request.session.get('user_id')
	user_name = request.session.get('user_name')
	hefu_count = sviews.ret_info()
	if request.method == 'GET':
		SoftModuleData = Modules.objects.all()
		GroupData = MinionGroup.objects.all()
		groupall = []
		for g in GroupData:
			group = {}
			list = []
			for m in g.minions.all():
				dir = {}
				dir['text'] = m.minion
				dir['id'] = m.minion
				list.append(dir)
		
			group['type'] = g.id
			group['list'] = list
			groupall.append(group)
		groupall = json.dumps(groupall)
		return render(request, template, locals())
	else:
		if not request.POST.get('minion'):
			minions_id = request.POST.get('minion_group')
			minions_data = MinionGroup.objects.get(id=minions_id).minions.all()
		else:
			minions_data = request.POST.getlist('minion')
		
		minions_list = ''
		for m in minions_data:
			minions_list += str(m) + ','
		minions_list = minions_list.strip(',')
		
		software = request.POST.getlist('software')
		salt_env = request.POST.get('env')
		
		soft = ''
		for i in software:
			soft += i + ','
		soft = soft.strip(',')
		
		saltm = Minions.objects.get(minion=minions_list.split(',')[0])
		
		url = saltm.saltserver.url
		username = saltm.saltserver.username
		password = saltm.saltserver.password
		
		salt = SaltApi(url, username, password)
		
		jid = salt.Softwarete_deploy(minions_list, arg=["saltenv=%s" % (salt_env), str(soft), 'test=True'])
		
		Operation.objects.create(Opuser=user_name, Opaction=u'部署软件 %s' % soft)
		
		ret = {'jid': jid, 'minion': minions_list, 'savelogid': 1}
		return HttpResponse(json.dumps(ret))
def SoftInstall(request):
    usersession = request.session.get('user_id')
    user_name = request.session.get('user_name')
    if request.method == 'GET':
        SoftModuleData = Modules.objects.all()
        GroupData = MinionGroup.objects.all()
        groupall = []
        for g in GroupData:
            group = {}
            list = []
            for m in g.minions.all():
                dir = {}
                dir['text'] = m.minion
                dir['id'] = m.minion
                list.append(dir)
            group['type'] = g.id
            group['list'] = list
            groupall.append(group)
        groupall = json.dumps(groupall)
        return render(request,'saltadmin/saltmodule_deploy.html',locals())
    else:
        if not request.POST.get('minion'):
            minions_id = request.POST.get('minion_group')
            minions_data=MinionGroup.objects.get(id=minions_id).minions.all()
        else:
            minions_data = request.POST.getlist('minion')
        minions_list = ''
        for m in minions_data:
            minions_list += str(m) + ','
        minions_list = minions_list.strip(',')
        software = request.POST.getlist('software')
        salt_env = request.POST.get('env')
        soft=''
        for i in software:
            soft += i + ','
        soft=soft.strip(',')
        saltm = Minions.objects.get(minion=minions_list.split(',')[0])
        url = saltm.saltserver.url
        username = saltm.saltserver.username
        password = saltm.saltserver.password
        salt = SaltApi(url, username, password)
        jid = salt.Softwarete_deploy(minions_list,arg=["saltenv=%s" %(salt_env), str(soft), 'test=True'])
        Operation.objects.create(Opuser=user_name, Opaction=u'部署软件 %s' %soft)
        #savelog = CmdRunLog.objects.create(user=user_name, target=minions_list, cmd=cmd, total=len(minions_list.split(',')))
        ret={'jid':jid,'minion':minions_list,'savelogid':1}
        return  HttpResponse(json.dumps(ret))