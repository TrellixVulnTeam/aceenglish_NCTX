# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-02-19 09:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20180219_1334'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='cert',
            field=models.ImageField(blank=True, null=True, upload_to='thanh-tich'),
        ),
        migrations.AddField(
            model_name='post',
            name='review',
            field=models.ImageField(blank=True, null=True, upload_to='thanh-tich'),
        ),
        migrations.AlterField(
            model_name='post',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='thanh-tich'),
        ),
    ]