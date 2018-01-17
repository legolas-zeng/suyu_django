# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.test import TestCase

# Create your tests here.

import re

s = '1079,1084,1089'
p = re.compile(r'\d,\d')

while 1:
	m = p.search(s)
	if m:
		mm = m.group()
		s = s.replace(mm, mm.replace(',', ''))
	else:
		break
print s
