# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-03-24 06:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20170323_1351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pat',
            name='user_name',
            field=models.CharField(default='kem cho', max_length=100),
        ),
    ]
