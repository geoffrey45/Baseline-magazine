# Generated by Django 3.0 on 2020-07-01 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magazine', '0052_auto_20200701_0514'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='slug',
            field=models.SlugField(default='', unique=True),
            preserve_default=False,
        ),
    ]
