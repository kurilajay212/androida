# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-04-04 11:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20170324_1428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pat',
            name='user_name',
            field=models.CharField(max_length=100),
        ),
    ]