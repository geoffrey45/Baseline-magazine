# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-06-28 11:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magazine', '0041_auto_20200628_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, default='articles/yhb5DBT91u4_Regular.jpg', upload_to='articles'),
        ),
    ]
