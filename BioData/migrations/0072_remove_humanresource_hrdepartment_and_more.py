# Generated by Django 5.0.6 on 2024-08-24 11:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BioData', '0071_remove_task_taskassignedto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='humanresource',
            name='HRDepartment',
        ),
        migrations.RemoveField(
            model_name='humanresource',
            name='HREmail',
        ),
        migrations.RemoveField(
            model_name='humanresource',
            name='HRRole',
        ),
        migrations.RemoveField(
            model_name='humanresource',
            name='HRStatus',
        ),
        migrations.RemoveField(
            model_name='humanresource',
            name='HRTasks',
        ),
        migrations.RemoveField(
            model_name='humanresource',
            name='TaskIds',
        ),
        migrations.RemoveField(
            model_name='humanresource',
            name='created',
        ),
    ]