# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-19 10:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('saltstack', '0026_auto_20171218_2004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='minions',
            name='saltserver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='saltstack.saltserver', verbose_name='\u6240\u5c5eSalt\u670d\u52a1\u5668'),
        ),
    ]
