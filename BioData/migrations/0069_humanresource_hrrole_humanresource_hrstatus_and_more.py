# Generated by Django 5.0.6 on 2024-08-24 11:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BioData', '0068_alter_task_taskstatus'),
    ]

    operations = [
        migrations.AddField(
            model_name='humanresource',
            name='HRRole',
            field=models.CharField(choices=[('Doctor', 'Doctor'), ('Psychologist', 'Psychologist'), ('Nutritionist', 'Nutritionist'), ('Care Manager', 'Care Manager'), ('Engagement Lead', 'Engagement Lead')], default='Care Manager', max_length=50),
        ),
        migrations.AddField(
            model_name='humanresource',
            name='HRStatus',
            field=models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive'), ('On Leave', 'On Leave')], default='Active', max_length=50),
        ),
        migrations.AddField(
            model_name='humanresource',
            name='TaskIds',
            field=models.ManyToManyField(blank=True, related_name='TaskIds', to='BioData.task'),
        ),
        migrations.AlterField(
            model_name='task',
            name='taskAssignedTo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='taskAssignedTo', to='BioData.humanresource'),
        ),
    ]
