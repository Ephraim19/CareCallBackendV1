# Generated by Django 5.0.6 on 2024-08-10 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BioData', '0053_alter_temperature_readingdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='oxygen',
            name='interpretation',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
