# Generated by Django 5.0.6 on 2024-08-24 11:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BioData', '0070_alter_task_taskassignedto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='taskAssignedTo',
        ),
    ]