# Generated by Django 5.0.6 on 2024-07-30 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BioData', '0037_task'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='taskDepartment',
            field=models.CharField(default='Doctor', max_length=50),
            preserve_default=False,
        ),
    ]
