# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-06-13 10:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postgres', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arrayfielddefinition',
            name='size',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='size'),
        ),
    ]
