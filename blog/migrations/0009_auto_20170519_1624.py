# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-19 08:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20170515_2128'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='pid',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='post',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='user',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]