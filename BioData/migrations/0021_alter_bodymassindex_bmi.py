# Generated by Django 5.0.6 on 2024-06-27 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BioData', '0020_alter_bodymassindex_bmi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bodymassindex',
            name='bmi',
            field=models.IntegerField(),
        ),
    ]
