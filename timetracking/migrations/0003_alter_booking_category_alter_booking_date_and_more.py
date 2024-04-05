# Generated by Django 5.0.4 on 2024-04-05 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetracking', '0002_alter_booking_end_time_alter_booking_start_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='category',
            field=models.CharField(choices=[('Work', 'Work'), ('Break', 'Break'), ('Job search', 'Job search'), ('Leisure', 'Leisure'), ('Vacation', 'Vacation'), ('Illness', 'Illness'), ('Other', 'Other')], default='Work', max_length=20),
        ),
        migrations.AlterField(
            model_name='booking',
            name='date',
            field=models.DateField(verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='end_time',
            field=models.TimeField(verbose_name='Ending time'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='start_time',
            field=models.TimeField(verbose_name='Starting time'),
        ),
    ]
