# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-07 13:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('example_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='make',
            name='exprice',
            field=models.DecimalField(blank=True, decimal_places=3, default=0, max_digits=30, null=True),
        ),
        migrations.AddField(
            model_name='make',
            name='start_date',
            field=models.CharField(blank=True, max_length=122100, null=True),
        ),
    ]
