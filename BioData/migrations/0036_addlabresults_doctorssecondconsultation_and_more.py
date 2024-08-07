# Generated by Django 5.0.6 on 2024-07-03 10:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BioData', '0035_initialconsultationdoctor_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddLabResults',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('taskDate', models.DateField()),
                ('status', models.CharField(default='Not started', max_length=20)),
                ('department', models.CharField(blank=True, max_length=20, null=True)),
                ('assignedTo', models.CharField(blank=True, max_length=50, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('memberId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BioData.member')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DoctorsSecondConsultation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('taskDate', models.DateField()),
                ('status', models.CharField(default='Not started', max_length=20)),
                ('department', models.CharField(blank=True, max_length=20, null=True)),
                ('assignedTo', models.CharField(blank=True, max_length=50, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('memberId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BioData.member')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GenerateCarePlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('taskDate', models.DateField()),
                ('status', models.CharField(default='Not started', max_length=20)),
                ('department', models.CharField(blank=True, max_length=20, null=True)),
                ('assignedTo', models.CharField(blank=True, max_length=50, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('memberId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BioData.member')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GenerateLabRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('taskDate', models.DateField()),
                ('status', models.CharField(default='Not started', max_length=20)),
                ('department', models.CharField(blank=True, max_length=20, null=True)),
                ('assignedTo', models.CharField(blank=True, max_length=50, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('memberId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BioData.member')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ScheduleAnnualLabTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('taskDate', models.DateField()),
                ('status', models.CharField(default='Not started', max_length=20)),
                ('department', models.CharField(blank=True, max_length=20, null=True)),
                ('assignedTo', models.CharField(blank=True, max_length=50, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('memberId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BioData.member')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ScheduleResultsReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('taskDate', models.DateField()),
                ('status', models.CharField(default='Not started', max_length=20)),
                ('department', models.CharField(blank=True, max_length=20, null=True)),
                ('assignedTo', models.CharField(blank=True, max_length=50, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('memberId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BioData.member')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
