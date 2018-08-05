# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-05 16:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=12)),
                ('pwd', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=30)),
                ('show', models.CharField(max_length=20, null=True)),
                ('address', models.CharField(max_length=50, null=True)),
                ('youbian', models.CharField(max_length=50, null=True)),
                ('phone', models.CharField(max_length=11, null=True)),
            ],
            options={
                'db_table': 'ttsx_user',
            },
        ),
        migrations.CreateModel(
            name='UserTicket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticket', models.CharField(max_length=256)),
                ('out_time', models.DateTimeField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.UserModel')),
            ],
            options={
                'db_table': 'ttsx_user_ticket',
            },
        ),
    ]