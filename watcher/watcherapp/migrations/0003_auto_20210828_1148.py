# Generated by Django 3.1 on 2021-08-28 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watcherapp', '0002_auto_20210828_1146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='active',
            name='active_ip',
            field=models.TextField(blank=True, max_length=16),
        ),
        migrations.AlterField(
            model_name='metrix',
            name='metrix_ram',
            field=models.TextField(default=None, max_length=254),
        ),
    ]
