# Generated by Django 3.1.3 on 2020-11-14 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0005_auto_20201114_0320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='movie_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
