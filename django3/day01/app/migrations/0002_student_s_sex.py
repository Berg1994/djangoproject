# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-10 01:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='s_sex',
            field=models.BooleanField(default=1),
        ),
    ]
