# Generated by Django 5.0.6 on 2024-08-24 12:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BioData', '0073_task_taskassignedto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='taskAssignedTo',
        ),
        migrations.DeleteModel(
            name='HumanResource',
        ),
    ]
