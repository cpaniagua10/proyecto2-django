# Generated by Django 3.1.3 on 2020-11-15 06:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0013_seat_full'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='time',
        ),
    ]