# Generated by Django 3.0 on 2020-07-03 13:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('magazine', '0056_auto_20200702_2157'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='tag',
        ),
        migrations.DeleteModel(
            name='tags',
        ),
    ]
