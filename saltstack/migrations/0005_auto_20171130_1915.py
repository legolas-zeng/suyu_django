# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-30 19:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('saltstack', '0004_auto_20171130_1857'),
    ]

    operations = [
        migrations.CreateModel(
            name='Modules',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Salt\u6a21\u5757\u540d\u79f0')),
                ('models_site', models.CharField(blank=True, max_length=50, null=True, verbose_name='Salt\u6a21\u5757\u53c2\u6570')),
            ],
            options={
                'verbose_name': 'Salt\u8f6f\u4ef6',
                'verbose_name_plural': 'Salt\u8f6f\u4ef6',
            },
        ),
        migrations.AlterField(
            model_name='minions',
            name='saltserver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='saltstack.saltserver', verbose_name='\u6240\u5c5eSalt\u670d\u52a1\u5668'),
        ),
    ]
