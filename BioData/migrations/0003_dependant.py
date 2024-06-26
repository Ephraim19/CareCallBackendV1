# Generated by Django 4.2.13 on 2024-05-15 09:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BioData', '0002_member_membercaremanager_member_memberemployer_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dependant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('depandantName', models.CharField(max_length=50)),
                ('dependantAge', models.IntegerField()),
                ('dependantRelationship', models.CharField(max_length=10)),
                ('dependantStatus', models.CharField(max_length=10)),
                ('dependantId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BioData.member')),
            ],
        ),
    ]
