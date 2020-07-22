# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-28 17:16
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
                ('role', models.CharField(choices=[('main', 'main'), ('subordinate', 'subordinate')], default='subordinate', max_length=30, verbose_name='\u89d2\u8272')),
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
                ('hefuid', models.CharField(max_length=255, unique=True, verbose_name='\u5408\u670d\u8ba2\u5355\u53f7')),
                ('ip', models.GenericIPAddressField(default='0.0.0.0', verbose_name='\u4e3b\u670dip')),
                ('game', models.CharField(default='golden', max_length=255, verbose_name='\u6e38\u620f\u7248\u672c')),
                ('platform', models.CharField(max_length=255, verbose_name='\u5e73\u53f0')),
                ('area', models.CharField(max_length=255, verbose_name='\u533a\u670d\u53f7')),
                ('server_id', models.CharField(max_length=255, verbose_name='\u4e3b\u670dID')),
                ('server_ids', models.CharField(max_length=255, verbose_name='\u5408\u5e76\u670dID')),
                ('apply_time', models.DateTimeField(max_length=255, verbose_name='\u7533\u8bf7\u65f6\u95f4')),
                ('status', models.CharField(max_length=255, verbose_name='\u8ba2\u5355\u72b6\u6001')),
                ('combine_time', models.DateTimeField(max_length=255, verbose_name='\u5408\u670d\u65f6\u95f4')),
                ('progress', models.CharField(default=0, max_length=255, verbose_name='\u5408\u670d\u8fdb\u5ea6')),
                ('success', models.IntegerField(default=0, verbose_name='\u662f\u5426\u5b8c\u6210')),
                ('main_server_ip', models.GenericIPAddressField(default='0.0.0.0')),
            ],
            options={
                'verbose_name': '\u5408\u670d\u5217\u8868',
                'verbose_name_plural': '\u5408\u670d\u8be6\u60c5',
            },
        ),
        migrations.CreateModel(
            name='new_game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('new_game_id', models.CharField(max_length=255, verbose_name='\u65b0\u670d\u8ba2\u5355\u53f7')),
                ('platform', models.CharField(max_length=255, verbose_name='\u5e73\u53f0')),
                ('game', models.CharField(max_length=255)),
                ('area', models.CharField(default=0, max_length=16, verbose_name='\u6e38\u620f\u7f16\u53f7')),
                ('game_id', models.CharField(max_length=255, verbose_name='\u552f\u4e00ID')),
                ('open_date', models.DateTimeField(max_length=255, verbose_name='\u5f00\u670d\u65f6\u95f4')),
                ('apply_date', models.DateTimeField(max_length=255, verbose_name='\u7533\u8bf7\u65f6\u95f4')),
                ('sate', models.BooleanField(default=1, max_length=2, verbose_name='\u72b6\u6001')),
                ('progress', models.CharField(default=0, max_length=255, verbose_name='\u5b89\u88c5\u8fdb\u5ea6')),
                ('success', models.IntegerField(default=0, verbose_name='\u662f\u5426\u5b8c\u6210')),
                ('ip', models.GenericIPAddressField(default='0.0.0.0', verbose_name='\u5206\u914dip')),
                ('name', models.CharField(max_length=255, verbose_name='\u533a\u670d\u540d\u79f0')),
            ],
            options={
                'verbose_name': '\u65b0\u670d\u8be6\u60c5',
                'verbose_name_plural': '\u65b0\u670d\u7533\u8bf7',
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
        migrations.CreateModel(
            name='server',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('platform', models.CharField(max_length=255, verbose_name='\u5e73\u53f0')),
                ('area', models.CharField(default=0, max_length=16, verbose_name='\u6e38\u620f\u7f16\u53f7')),
                ('app', models.CharField(max_length=16, verbose_name='\u4e2d\u5fc3\u670d')),
                ('app_id', models.CharField(max_length=255, verbose_name='\u6e38\u620f\u7c7b')),
                ('server', models.CharField(max_length=255, verbose_name='\u552f\u4e00ID')),
                ('merge', models.CharField(max_length=255, verbose_name='\u5408\u5e76\u533a\u670d')),
                ('name', models.CharField(max_length=255, verbose_name='\u533a\u670d\u540d\u79f0')),
                ('game', models.CharField(max_length=255)),
                ('show', models.CharField(max_length=16, verbose_name='\u663e\u793a\u53f7')),
                ('status', models.CharField(max_length=16)),
                ('offtime', models.DateTimeField(max_length=255, verbose_name='\u505c\u670d\u65f6\u95f4')),
                ('sertime', models.DateTimeField(max_length=255, verbose_name='\u5f00\u670d\u65f6\u95f4')),
                ('ip', models.GenericIPAddressField(verbose_name='IP')),
                ('white', models.CharField(max_length=16, verbose_name='\u767d\u540d\u5355')),
                ('is_open', models.BooleanField(max_length=2, verbose_name='\u662f\u5426\u5f00\u670d')),
                ('add_time', models.CharField(max_length=255, verbose_name='\u7533\u8bf7\u65f6\u95f4')),
            ],
            options={
                'verbose_name': '\u6e38\u620f\u5217\u8868',
                'verbose_name_plural': '\u6e38\u620f\u8be6\u60c5',
            },
        ),
    ]
