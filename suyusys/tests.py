# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

# Create your tests here.
from suyusys.models import *

now_id_ob = hefuinfo.objects.order_by("hefuid")[0:1].get()
print now_id_ob