# Generated by Django 5.0.6 on 2024-08-26 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BioData', '0082_alter_appointments_appointmentassignedto_whatsapp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='whatsapp',
            name='messageFrom',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
