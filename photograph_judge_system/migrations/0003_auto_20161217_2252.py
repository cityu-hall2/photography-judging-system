# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-17 22:52
from __future__ import unicode_literals

from django.db import migrations, models
import photograph_judge_system.models


class Migration(migrations.Migration):

    dependencies = [
        ('photograph_judge_system', '0002_judge_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='full_size_url',
            field=models.CharField(default=' ', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='photo',
            name='thumbnail_url',
            field=models.CharField(default=' ', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='judge',
            name='password',
            field=models.CharField(default=photograph_judge_system.models.random_password, max_length=20),
        ),
    ]