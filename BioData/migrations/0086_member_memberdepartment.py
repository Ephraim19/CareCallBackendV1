# Generated by Django 5.0.6 on 2024-08-31 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BioData', '0085_alter_whatsapp_messagestatus'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='memberDepartment',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
