# Generated by Django 3.0.7 on 2020-06-24 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magazine', '0004_auto_20200624_1015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='photo_credits',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
