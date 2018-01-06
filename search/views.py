# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,redirect,render_to_response
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
import re
from suyusys import views


# Create your views here.

def ip_search(request):
	if request.method=='GET':
		key_word = request.GET['top-search']
		print key_word
		return HttpResponseRedirect(reverse('action_search',kwargs={"key_word":123}))
		#return HttpResponseRedirect(reverse('suyusys:action_search',args=(key_word,)))
