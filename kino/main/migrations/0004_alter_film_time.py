# Generated by Django 5.0 on 2023-12-23 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_film_hall_film_time_alter_film_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='time',
            field=models.TimeField(),
        ),
    ]