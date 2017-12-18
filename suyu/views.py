# -*- coding: utf-8 -*-
from __future__ import unicode_literals
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
from function import handle_uploaded_file
from .forms import LoginForm
from forms import UploadFileForm
import json
import datetime
import os
from salt_run import *

def index(request,template='index.html'):
    btime = '2017-09-09 00:00'
    idc_list = IDC.objects.all()
    host_list = autohost.objects.filter(autoTime__gte=btime)
    context = {
        'idc_list': idc_list,
        'host_list': host_list,
    }
    return render(request,template,context)
def hostlistinfo(request,template='hostlistinfo.html'):
    idc_list = IDC.objects.all()
    host_list = Host.objects.all()
    test_list = autohost.objects.all()
    context = {
        'idc_list': idc_list,
        'host_list': host_list,
        'test_list': test_list
    }
    return render(request, template, context)
def base(request,template='base.html'):
    return render(request, template)
def login(request,template='login.html'):
    msg = ''
    next = request.GET.get('next', '')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        next = request.POST['next']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                #login(request, user)
                if next:
                    return HttpResponseRedirect(next)
                return HttpResponseRedirect(reverse('index'))
            else:
                msg = u"用户已禁用"
        else:
            msg = u'用户名或者密码错误'
    context = {
        'msg': msg,
        'next': next,
    }
    return render(request,template,context)
@csrf_exempt
def apireport(request,templata='apireport.html'):
    if request.method=='POST':
        req=json.loads(request.body)
        hostdata=list()
        print req
        hostname=req.get('hostname')
        ip=req.get('ip')
        disk=req.get('disk')
        cpucore = req.get('cpucore')
        cached = req.get('cached')
        buffer = req.get('buffer')
        swap = req.get('swap')
        hostdata.append(autohost(autohostname=hostname,autoip=ip,autodisk=disk,autocpucore=cpucore,mencached=cached,menbuffer=buffer,menswap=swap))
        autohost.objects.bulk_create(hostdata)
    return HttpResponse('1')
    #return render(request,templata)
@csrf_exempt
def apichart(request,template='apichart.html'):
    btime='2017-09-09 00:00'
    line_dict = {'categories': [], 'data': []}
    cpuid=autohost.objects.filter(autoTime__gte=btime)
    for line in cpuid:
        line_dict['categories'].append(line.autoTime.strftime('%Y-%m-%d %H:%M'))
        line_dict['data'].append(line.autocpucore)
    #return HttpResponse(json.dumps(line_dict))
    return JsonResponse(line_dict)
@csrf_exempt
def chart(request,template='chart.html'):
    idc_list = IDC.objects.all()
    host_info= Host.objects.all()
    context = {
        'idc_list': idc_list,
        'host_info': host_info,
    }
    return render(request, template, context)
def bad (request,template='bad.html'):
    btime = '2017-09-09 00:00'
    idc_list = IDC.objects.all()
    host_list = autohost.objects.filter(autoTime__gte=btime)
    context = {
        'idc_list': idc_list,
        'host_list': host_list,
    }
    return render(request,template,context)
def test (request,template='test.html'):
    return render(request,template)
def test_2(request,template='test_2.html'):
    return render(request,template)
def test_2_api(request):
    return  HttpResponse(1)
def test_3 (request,template='test_3.html'):
    return render(request,template)
@csrf_exempt
# 单文件上传
def test_4(request,template='test_4.html'):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            f=handle_uploaded_file(request.FILES['file'])
            upload_file = request.FILES['file']
            upload=list()
            upload.append(uploadfile(filetitle=f[0], filepath=f[1],filesize=f[2]))
            uploadfile.objects.bulk_create(upload)
            return HttpResponse('上传成功')
        else:
            return HttpResponse('上传失败')
    else:
        form = UploadFileForm()
    context = {
        'form': form,
    }
    return render(request,'test_4.html',context)
@csrf_exempt
# 多文件上传
def test_5(request,template='test_5.html'):
    if request.method=='POST':
        a = request.FILES.getlist('file')
        for afile in request.FILES.getlist('file'):
            form = UploadFileForm(request.POST, request.FILES)
            if form.is_valid():
                f = handle_uploaded_file(afile)
                size = len(afile.read())
                title = f[0]
                path = f[1].decode('gbk')
                upload = list()
                upload.append(uploadfile(filetitle=f[0], filepath=f[1],filesize=f[2]))
                uploadfile.objects.bulk_create(upload)
        return HttpResponse('多文件上传成功')
    else:
        form = UploadFileForm()
    context = {
        'form': form,
    }
    return render(request, 'test_5.html', context)

@csrf_exempt
def test_6(request,template='test_6.html'):
    files = uploadfile.objects.all()
    context = {
        'files': files,
    }
    return render(request, template, context)
         
def apimen(request,template='apimen.html'):
	btime = '2017-09-09 00:00'
	line_dict = {'categories': [], 'bad': [],'buffer': [],'swap': []}
	men=autohost.objects.filter(autoTime__gte=btime)
	for line in men:
		line_dict['categories'].append(line.autoTime.strftime('%Y-%m-%d %H:%M'))
		line_dict['bad'].append(line.mencached)
		line_dict['buffer'].append(line.menbuffer)
		line_dict['swap'].append(line.menswap)
	return JsonResponse(line_dict)
@csrf_exempt
def server_upload(request,template='upload.html'):
    return render(request,template)
@csrf_exempt
def uploadsave(request,template='uploadsave.html'):
    try:
        f = handle_uploaded_file(request.FILES['file'])
        print f
        upload = list()
        upload.append(uploadfile(filetitle=f[0], filepath=f[1],filesize=f[2]))
        uploadfile.objects.bulk_create(upload)
        input_file = request.FILES['file']
        filename = input_file.name
        BASE_DIR = 'F:\django_test'
        path = os.path.join(BASE_DIR, 'media\\')
        file_name = os.path.join(path, filename.decode('utf-8'))
        return HttpResponse(json.dumps({'flag_succeed': 'true', 'filename': filename, 'file_url': file_name, }))
    except Exception as e:
        return HttpResponse(json.dumps({'error': e,}))
def upload_list(request,template='upload_list.html'):
    files = uploadfile.objects.all()
    context = {
        'files': files,
    }
    return render(request,template,context)
@csrf_exempt
def upload_del(request,template='test_6.html'):
    if request.method=='POST':
        fileid_list = json.loads(request.body)
        #fileid=request.POST.get(request.body)
        files_info = []
        print fileid_list
        print type(fileid_list)
        for fileid in fileid_list:
            for fileid in fileid_list[fileid]:
                print fileid
                file = uploadfile.objects.filter(id=fileid).values()
                for fileinfo in file:
                    filepath = fileinfo['filepath']
                    filename = fileinfo['filetitle']
                    del_file = os.path.join(filepath, filename)
                    print del_file
                    if os.path.isdir(filepath):
                        if os.path.isfile(del_file):
                            os.remove(del_file)
                            uploadfile.objects.filter(id=fileid).update(fileexit=False)
                            # context = {'msg': u'文件'+fileid+u'已删除'}
                            context=u'文件'+fileid+u'已删除'
                        else:
                            # context = {'msg': u'文件'+fileid+u'不存在'}
                            context = u'文件'+fileid+u'不存在'
                    else:
                        print u"路径错误"
                        # context = {'msg': u'文件'+fileid+u'路径错误'}
                    print context
                    files_info.append(context)
                    print files_info
            context = {'msg' : files_info}
            # return JsonResponse(files_info,safe=False)
            return  JsonResponse(context)
@csrf_exempt
def redisreport(request,template='redisreport.html'):
    if request.method=='POST':
        req=json.loads(request.body)
        redisdata=list()
        print req
        ip=req.get('ip')
        print ip
        alive=req.get('alive')
        role=req.get('role')
        connected = req.get('connected')
        redisdata.append(Redisinfotest(hostip=ip,role=role,alive=alive,connected=connected))
        Redisinfotest.objects.bulk_create(redisdata)
        
        T=DbServersRedis.objects.get(hostip=ip)
        T.role = role
        T.save()
        '''这里还需要写存储'''
    return HttpResponse('1')


                
    
        
    
    
    







