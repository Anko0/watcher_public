# Generated by Django 3.1 on 2021-08-28 09:15

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Active',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active_name', models.CharField(max_length=50)),
                ('active_token', models.CharField(max_length=256)),
                ('active_hostname', models.CharField(blank=True, max_length=50)),
                ('active_ip', models.FloatField(blank=True, max_length=16)),
                ('active_description', models.TextField(blank=True)),
                ('active_created', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Metrix',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('metrix_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('metrix_cpu', models.CharField(default=None, max_length=254)),
                ('metrix_ram', models.EmailField(default=None, max_length=254)),
                ('metrix_rom', models.CharField(default=None, max_length=1024)),
                ('metrix_proc', models.TextField(blank=True)),
                ('metrix_uname', models.CharField(default=None, max_length=254)),
                ('metrix_users', models.CharField(default=None, max_length=254)),
                ('metrix_active', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='watcherapp.active')),
            ],
        ),
    ]
