# Generated by Django 5.0.4 on 2024-04-05 19:32

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date', models.DateField(verbose_name='Datum')),
                ('start_time', models.DateTimeField(verbose_name='Startzeit')),
                ('end_time', models.DateTimeField(verbose_name='Endzeit')),
                ('category', models.CharField(choices=[('Arbeit', 'Arbeit'), ('Pause', 'Pause'), ('Jobsuche', 'Jobsuche'), ('Freizeit', 'Freizeit'), ('Urlaub', 'Urlaub'), ('Krankheit', 'Krankheit'), ('Sonstiges', 'Sonstiges')], default='Arbeit', max_length=20)),
                ('comment', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Nutzer')),
            ],
        ),
    ]
