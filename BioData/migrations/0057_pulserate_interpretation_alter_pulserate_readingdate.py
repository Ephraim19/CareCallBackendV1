# Generated by Django 5.0.6 on 2024-08-11 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BioData', '0056_alter_oxygen_readingdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='pulserate',
            name='interpretation',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='pulserate',
            name='readingDate',
            field=models.CharField(max_length=100),
        ),
    ]
