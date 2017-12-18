# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-18 19:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DbServersRedis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostip', models.GenericIPAddressField(default='0.0.0.0', verbose_name='\u4e3b\u673aIP')),
                ('port', models.CharField(max_length=10, verbose_name='\u7aef\u53e3')),
                ('monitor', models.CharField(choices=[('Ture', 'ON'), ('False', 'OFF')], default='Ture', max_length=30, null=True, verbose_name='\u662f\u5426\u5f00\u542f\u76d1\u63a7')),
                ('tags', models.CharField(blank=True, max_length=50, null=True)),
                ('role', models.CharField(choices=[('master', 'master'), ('slave', 'slave')], default='slave', max_length=30, verbose_name='\u89d2\u8272')),
                ('alive', models.BooleanField(default=False, verbose_name='\u662f\u5426\u5728\u7ebf')),
                ('connected', models.CharField(default=0, max_length=255, verbose_name='\u8fde\u63a5\u6570')),
            ],
            options={
                'verbose_name': '\u76d1\u63a7\u4e3b\u673a',
                'verbose_name_plural': 'redis\u76d1\u63a7\u673a\u7ec4',
            },
        ),
        migrations.CreateModel(
            name='hefuinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heufid', models.CharField(max_length=255, unique=True, verbose_name='\u5408\u670d\u8ba2\u5355\u53f7')),
                ('game', models.CharField(default='golden', max_length=255, verbose_name='\u6e38\u620f\u7248\u672c')),
                ('platform', models.CharField(max_length=255, verbose_name='\u5e73\u53f0')),
                ('area', models.CharField(max_length=255, verbose_name='\u533a\u670d\u53f7')),
                ('server_id', models.CharField(max_length=255, verbose_name='\u4e3b\u670dID')),
                ('server_ids', models.CharField(max_length=255, verbose_name='\u5408\u5e76\u670dID')),
                ('apply_time', models.DateTimeField(max_length=255, verbose_name='\u7533\u8bf7\u65f6\u95f4')),
                ('status', models.CharField(max_length=255, verbose_name='\u8ba2\u5355\u72b6\u6001')),
                ('combine_time', models.DateTimeField(max_length=255, verbose_name='\u5408\u670d\u65f6\u95f4')),
                ('progress', models.CharField(default=0, max_length=255, verbose_name='\u5408\u670d\u8fdb\u5ea6')),
                ('success', models.BooleanField(default=False, verbose_name='\u662f\u5426\u5b8c\u6210')),
            ],
            options={
                'verbose_name': '\u5408\u670d\u5217\u8868',
                'verbose_name_plural': '\u5408\u670d\u8be6\u60c5',
            },
        ),
        migrations.CreateModel(
            name='Redisinfotest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostip', models.GenericIPAddressField(default='0.0.0.0')),
                ('role', models.CharField(max_length=255)),
                ('alive', models.BooleanField(default=False)),
                ('connected', models.CharField(default=0, max_length=255)),
                ('autoTime', models.DateTimeField(auto_now_add=True, verbose_name='\u4e0a\u62a5\u65f6\u95f4')),
            ],
        ),
    ]
