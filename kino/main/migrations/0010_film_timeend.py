# Generated by Django 5.0 on 2023-12-24 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_alter_hall_seats'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='timeEnd',
            field=models.TimeField(auto_now=True),
        ),
    ]