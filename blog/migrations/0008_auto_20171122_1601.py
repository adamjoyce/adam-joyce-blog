# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-22 16:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20171122_1555'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='first_name',
            field=models.CharField(default='first_name', max_length=15),
        ),
        migrations.AddField(
            model_name='author',
            name='last_name',
            field=models.CharField(default='second_name', max_length=15),
        ),
    ]
