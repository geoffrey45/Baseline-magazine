# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-06-25 23:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magazine', '0014_remove_magazineapimodel_article_imagee'),
    ]

    operations = [
        migrations.AddField(
            model_name='magazineapimodel',
            name='article_imagee',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
