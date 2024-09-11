# Generated by Django 5.0.6 on 2024-09-11 16:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BioData', '0093_doctor'),
    ]

    operations = [
        migrations.CreateModel(
            name='BodyComposition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updatedBy', models.EmailField(max_length=254)),
                ('readingDate', models.CharField(max_length=100)),
                ('bodyFat', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('muscleMass', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('boneMass', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('visceralFat', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('DCI', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('metabolicAge', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('bodyWater', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('memberId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BioData.member')),
            ],
        ),
    ]
