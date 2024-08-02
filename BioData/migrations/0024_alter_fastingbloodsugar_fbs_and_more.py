# Generated by Django 5.0.6 on 2024-06-27 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BioData', '0023_alter_glycatedhaemoglobin_hba1c'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fastingbloodsugar',
            name='fbs',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='randombloodsugar',
            name='rbs',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
    ]