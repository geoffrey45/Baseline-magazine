# Generated by Django 3.0.7 on 2020-06-23 14:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('magazine', '0002_tag'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('post', models.TextField()),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('article_image', models.ImageField(upload_to='articles/')),
                ('editor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='magazine.Editor')),
                ('tags', models.ManyToManyField(to='magazine.tag')),
            ],
        ),
    ]