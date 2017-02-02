# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-02 03:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bike', '0004_auto_20170129_2220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bike',
            name='donated_at',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='bike',
            name='donated_by',
            field=models.TextField(blank=True, null=True),
        ),
    ]