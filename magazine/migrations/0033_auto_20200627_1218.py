# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-06-27 09:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magazine', '0032_auto_20200627_1213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(upload_to='articles'),
        ),
    ]