# Generated by Django 3.1.3 on 2020-11-14 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0006_auto_20201114_0322'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='seat_number',
            field=models.CharField(blank=True, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='movie',
            field=models.CharField(choices=[('1', 'movie-one'), ('2', 'movie-two'), ('3', 'movie-three')], max_length=9),
        ),
    ]
