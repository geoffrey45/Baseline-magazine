# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-06-26 14:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magazine', '0023_auto_20200626_1714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='tag',
            field=models.ManyToManyField(blank=True, to='magazine.tags'),
        ),
    ]