# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-06-26 03:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('magazine', '0021_auto_20200626_0608'),
    ]

    operations = [
        migrations.RenameField(
            model_name='magazineapimodel',
            old_name='article_imagee',
            new_name='article_image',
        ),
    ]