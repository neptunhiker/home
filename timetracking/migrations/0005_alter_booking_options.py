# Generated by Django 5.0.4 on 2024-04-06 17:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timetracking', '0004_alter_booking_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='booking',
            options={'ordering': ['-date', '-start_time']},
        ),
    ]