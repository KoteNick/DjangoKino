# Generated by Django 5.0 on 2023-12-23 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='title',
            field=models.TextField(max_length=30),
        ),
    ]