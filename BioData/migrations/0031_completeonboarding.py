# Generated by Django 5.0.6 on 2024-07-03 08:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BioData', '0030_alter_callmembers_department_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='completeOnboarding',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('taskDate', models.DateField()),
                ('status', models.CharField(default='Not started', max_length=20)),
                ('department', models.CharField(default='Care Manager', max_length=20)),
                ('assignedTo', models.CharField(default='', max_length=50)),
                ('notes', models.TextField(blank=True, null=True)),
                ('memberId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='onboarding', to='BioData.member')),
            ],
        ),
    ]
