# Generated by Django 2.2.1 on 2020-07-04 02:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Example1', '0006_auto_20200703_2136'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='example1',
            name='curp',
        ),
    ]
