# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-12 01:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('examination', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='physical',
            name='palpation_first',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='physical',
            name='palpation_second',
            field=models.DecimalField(decimal_places=1, default=0.0, max_digits=2),
            preserve_default=False,
        ),
    ]
