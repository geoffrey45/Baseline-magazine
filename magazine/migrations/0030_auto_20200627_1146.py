# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-06-27 08:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magazine', '0029_auto_20200627_1050'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='user',
        ),
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, upload_to='profile_pics'),
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]