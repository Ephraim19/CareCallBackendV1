# Generated by Django 5.0.6 on 2024-08-24 12:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BioData', '0075_humanresource_task_taskassignedto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='humanresource',
            name='HRDepartment',
        ),
    ]