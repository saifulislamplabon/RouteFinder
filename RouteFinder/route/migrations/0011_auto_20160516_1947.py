# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-16 19:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('route', '0010_remove_stopage_cost_from_source'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stopage',
            name='is_visited',
        ),
        migrations.RemoveField(
            model_name='stopage',
            name='previous_stopage',
        ),
    ]
