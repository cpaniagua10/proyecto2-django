# Generated by Django 3.1.3 on 2020-11-15 07:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0014_remove_ticket_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='movie_date',
        ),
    ]
