# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-12 21:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('block_ip', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blockip',
            name='banned_username',
            field=models.TextField(blank=True, null=True),
        ),
    ]
