# Generated by Django 5.0.4 on 2024-04-12 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobsearch', '0006_offer_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='headhunter',
            field=models.BooleanField(default=False),
        ),
    ]