# Generated by Django 3.1 on 2021-11-20 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watcherapp', '0016_auto_20211120_1207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='metrix',
            name='metrix_created',
            field=models.DateTimeField(),
        ),
    ]
