# Generated by Django 5.0.6 on 2024-08-24 12:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BioData', '0074_remove_task_taskassignedto_delete_humanresource'),
    ]

    operations = [
        migrations.CreateModel(
            name='HumanResource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('HRTasks', models.IntegerField(default=0)),
                ('HREmail', models.EmailField(max_length=254)),
                ('HRDepartment', models.CharField(max_length=50)),
                ('HRRole', models.CharField(choices=[('Doctor', 'Doctor'), ('Psychologist', 'Psychologist'), ('Nutritionist', 'Nutritionist'), ('Care Manager', 'Care Manager'), ('Engagement Lead', 'Engagement Lead')], default='Care Manager', max_length=50)),
                ('HRStatus', models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive'), ('On Leave', 'On Leave')], default='Active', max_length=50)),
                ('TaskId', models.ManyToManyField(blank=True, related_name='TaskId', to='BioData.task')),
            ],
        ),
        migrations.AddField(
            model_name='task',
            name='taskAssignedTo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='taskAssignedTo', to='BioData.humanresource'),
        ),
    ]
