# Generated by Django 2.2.7 on 2019-11-22 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_medicalinformation'),
    ]

    operations = [
        migrations.AddField(
            model_name='camper',
            name='other_companies_paying',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
