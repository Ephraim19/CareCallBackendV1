# Generated by Django 5.0.6 on 2024-08-31 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BioData', '0086_member_memberdepartment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='social',
            name='socialNotes',
            field=models.TextField(),
        ),
    ]
