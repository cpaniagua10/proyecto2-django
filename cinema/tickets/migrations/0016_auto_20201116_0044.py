# Generated by Django 3.1.3 on 2020-11-16 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0015_remove_ticket_movie_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seat',
            name='movie',
            field=models.CharField(choices=[('1', 'Black Panther'), ('2', 'Moonlight'), ('3', 'Aladdin')], max_length=9),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='movie',
            field=models.CharField(choices=[('1', 'Black Panther'), ('2', 'Moonlight'), ('3', 'Aladdin')], max_length=9),
        ),
    ]
