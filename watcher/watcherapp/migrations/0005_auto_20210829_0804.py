# Generated by Django 3.1 on 2021-08-29 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watcherapp', '0004_auto_20210828_1641'),
    ]

    operations = [
        migrations.AddField(
            model_name='metrix',
            name='metrix_swap',
            field=models.CharField(default=None, max_length=25400, null=True),
        ),
        migrations.AlterField(
            model_name='active',
            name='active_ip',
            field=models.CharField(blank=True, max_length=16),
        ),
        migrations.AlterField(
            model_name='metrix',
            name='metrix_ram',
            field=models.CharField(default=None, max_length=25400),
        ),
    ]
