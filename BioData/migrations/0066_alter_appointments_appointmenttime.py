# Generated by Django 5.0.6 on 2024-08-21 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BioData', '0065_appointments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointments',
            name='appointmentTime',
            field=models.CharField(max_length=100),
        ),
    ]
