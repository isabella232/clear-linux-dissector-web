# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-04-15 00:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('layerindex', '0040_versioncomparison_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='configopts',
            field=models.CharField(blank=True, max_length=4096),
        ),
    ]
