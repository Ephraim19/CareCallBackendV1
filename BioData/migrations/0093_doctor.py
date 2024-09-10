# Generated by Django 5.0.6 on 2024-09-10 08:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BioData', '0092_rename_pschologistdate_psychologist_psychologistdate'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('consultationType', models.TextField()),
                ('chiefComplaint', models.TextField()),
                ('medicalHistory', models.TextField()),
                ('reviewOfSystems', models.TextField()),
                ('diagnosis', models.TextField()),
                ('nextSteps', models.TextField()),
                ('updatedBy', models.EmailField(max_length=254)),
                ('comments', models.TextField()),
                ('consultationDate', models.CharField(max_length=50)),
                ('memberId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BioData.member')),
            ],
        ),
    ]