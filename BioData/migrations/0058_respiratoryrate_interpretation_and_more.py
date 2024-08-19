# Generated by Django 5.0.6 on 2024-08-11 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BioData', '0057_pulserate_interpretation_alter_pulserate_readingdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='respiratoryrate',
            name='interpretation',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='respiratoryrate',
            name='readingDate',
            field=models.CharField(max_length=100),
        ),
    ]