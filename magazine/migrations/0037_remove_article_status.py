# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-06-28 11:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('magazine', '0036_remove_article_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='status',
        ),
    ]