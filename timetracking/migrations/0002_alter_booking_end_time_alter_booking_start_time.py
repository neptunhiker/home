# Generated by Django 5.0.4 on 2024-04-05 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetracking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='end_time',
            field=models.TimeField(verbose_name='Endzeit'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='start_time',
            field=models.TimeField(verbose_name='Startzeit'),
        ),
    ]