# Generated by Django 3.1.3 on 2020-11-16 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0016_auto_20201116_0044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seat',
            name='movie',
            field=models.CharField(choices=[('Black Panther', 'Black Panther'), ('Moonligh', 'Moonlight'), ('Aladdin', 'Aladdin')], max_length=150),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='movie',
            field=models.CharField(choices=[('Black Panther', 'Black Panther'), ('Moonligh', 'Moonlight'), ('Aladdin', 'Aladdin')], max_length=150),
        ),
    ]