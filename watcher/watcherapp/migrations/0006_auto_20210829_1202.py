# Generated by Django 3.1 on 2021-08-29 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watcherapp', '0005_auto_20210829_0804'),
    ]

    operations = [
        migrations.AddField(
            model_name='metrix',
            name='metrix_netconn',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='metrix',
            name='metrix_netif',
            field=models.TextField(blank=True, null=True),
        ),
    ]
