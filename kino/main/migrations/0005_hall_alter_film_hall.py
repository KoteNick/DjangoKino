# Generated by Django 5.0 on 2023-12-23 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_film_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hall',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(max_length=1)),
            ],
        ),
        migrations.AlterField(
            model_name='film',
            name='hall',
            field=models.IntegerField(max_length=1),
        ),
    ]
