# Generated by Django 3.2.5 on 2021-07-19 06:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20210719_1204'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.RemoveField(
            model_name='users',
            name='author',
        ),
    ]
