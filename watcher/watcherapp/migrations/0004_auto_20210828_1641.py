# Generated by Django 3.1 on 2021-08-28 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watcherapp', '0003_auto_20210828_1148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='metrix',
            name='metrix_cpu',
            field=models.CharField(default=None, max_length=25400),
        ),
        migrations.AlterField(
            model_name='metrix',
            name='metrix_ram',
            field=models.TextField(default=None, max_length=25400),
        ),
        migrations.AlterField(
            model_name='metrix',
            name='metrix_rom',
            field=models.CharField(default=None, max_length=10240),
        ),
        migrations.AlterField(
            model_name='metrix',
            name='metrix_users',
            field=models.CharField(default=None, max_length=25400),
        ),
    ]