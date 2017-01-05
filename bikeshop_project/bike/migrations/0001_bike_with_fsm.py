# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-05 02:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import django_fsm


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('registration', '0002_auto_20161130_0157'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('colour', models.TextField()),
                ('make', models.TextField()),
                ('size', models.TextField(choices=[('C', 'child'), ('M', 'medium'), ('L', 'large'), ('XL', 'extra large')], max_length=2)),
                ('serial_number', models.TextField()),
                ('source', models.TextField(choices=[('COS_BIKE_DIVERSION_PILOT', 'City of Saskatoon Bike Diversion Pilot'), ('UOFS', 'University of Saskatchewan'), ('DROP_OFF', 'Drop Off')])),
                ('stripped', models.NullBooleanField()),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('state', django_fsm.FSMField(choices=[('RECEIVED', 'Received'), ('ASSESSED', 'Assessed'), ('AVAILABLE', 'CPIC Searched'), ('CLAIMED', 'Claimed'), ('SCRAPPED', 'Scrapped'), ('PURCHASED', 'Purchased'), ('TRANSFERRED_TO_POLICE', 'Transferred to police')], default='RECEIVED', max_length=50, protected=True)),
                ('stolen', models.NullBooleanField()),
                ('donated_by', models.TextField()),
                ('donated_at', models.DateField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('cpic_searched_at', models.DateTimeField(blank=True, null=True)),
                ('claimed_at', models.DateTimeField(blank=True, null=True)),
                ('last_worked_on', models.DateTimeField(blank=True, null=True)),
                ('purchased_at', models.DateTimeField(blank=True, null=True)),
                ('claimed_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='registration.Member')),
            ],
        ),
    ]
