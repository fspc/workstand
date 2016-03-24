# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-23 02:01
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('renewed_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('safe_space', models.BooleanField(default=False)),
                ('community', models.BooleanField(default=False)),
                ('space', models.BooleanField(default=False)),
                ('give_back', models.BooleanField(default=False)),
                ('acknowledgement', models.BooleanField(default=False)),
                ('member', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='membership', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]