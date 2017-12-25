# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-25 17:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suyusys', '0005_hefuinfo_main_server_ip'),
    ]

    operations = [
        migrations.CreateModel(
            name='server',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('platform', models.CharField(max_length=255, verbose_name='\u5e73\u53f0')),
                ('app', models.CharField(max_length=16, verbose_name='\u4e2d\u5fc3\u670d')),
                ('app_id', models.CharField(max_length=255, verbose_name='\u6e38\u620f\u7c7b')),
                ('server', models.CharField(max_length=255, verbose_name='\u552f\u4e00ID')),
                ('merge', models.CharField(max_length=255, verbose_name='\u5408\u5e76\u533a\u670d')),
                ('name', models.CharField(max_length=255, verbose_name='\u533a\u670d\u540d\u79f0')),
                ('game', models.CharField(max_length=255)),
                ('show', models.CharField(max_length=16, verbose_name='\u663e\u793a\u53f7')),
                ('status', models.CharField(max_length=16)),
                ('offtime', models.DateTimeField(max_length=255, verbose_name='\u505c\u670d\u65f6\u95f4')),
                ('pretip', models.DateTimeField(max_length=255, verbose_name='\u914d\u7f6e\u65f6\u95f4')),
                ('sertime', models.DateTimeField(max_length=255, verbose_name='\u5f00\u670d\u65f6\u95f4')),
                ('ip', models.GenericIPAddressField(verbose_name='IP')),
                ('white', models.CharField(max_length=16, verbose_name='\u767d\u540d\u5355')),
                ('is_open', models.BooleanField(max_length=2, verbose_name='\u662f\u5426\u5f00\u670d')),
                ('add_time', models.CharField(max_length=255, verbose_name='\u7533\u8bf7\u65f6\u95f4')),
                ('main_server_ip', models.GenericIPAddressField(default='0.0.0.0')),
            ],
        ),
    ]
