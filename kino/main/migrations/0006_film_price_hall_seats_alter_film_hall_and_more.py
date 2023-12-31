# Generated by Django 5.0 on 2023-12-23 19:17

import django.core.validators
import re
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_hall_alter_film_hall'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='price',
            field=models.IntegerField(default=100),
        ),
        migrations.AddField(
            model_name='hall',
            name='seats',
            field=models.CharField(default='[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]', max_length=200, validators=[django.core.validators.RegexValidator(re.compile('^\\d+(?:,\\d+)*\\Z'), code='invalid', message=None)]),
        ),
        migrations.AlterField(
            model_name='film',
            name='hall',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='hall',
            name='number',
            field=models.IntegerField(),
        ),
    ]
