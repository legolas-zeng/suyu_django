# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.test import TestCase

# Create your tests here.

from function import gameinfo

a = gameinfo()
c = 543
print type(c)
b = a.select(543)
print b