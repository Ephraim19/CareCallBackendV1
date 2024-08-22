# Generated by Django 5.0.6 on 2024-08-22 07:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BioData', '0066_alter_appointments_appointmenttime'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='taskAppointmentId',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='taskAppointmentId', to='BioData.appointments'),
        ),
        migrations.AlterField(
            model_name='task',
            name='taskStatus',
            field=models.CharField(choices=[('Not started', 'Not started'), ('Inprogress', 'Inprogress'), ('Cancelled', 'Cancelled'), ('Complete', 'Complete')], default='Not started', max_length=20),
        ),
    ]