# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-02 19:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('date', models.DateTimeField()),
                ('description', models.TextField()),
                ('location_lat', models.DecimalField(decimal_places=6, max_digits=9)),
                ('location_lng', models.DecimalField(decimal_places=6, max_digits=9)),
                ('marker_type', models.CharField(max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
