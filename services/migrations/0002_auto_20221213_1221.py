# Generated by Django 3.2.16 on 2022-12-13 12:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='created_on',
        ),
        migrations.RemoveField(
            model_name='service',
            name='date',
        ),
    ]