# Generated by Django 2.2.7 on 2019-12-05 02:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20191205_0236'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medicalinformation',
            name='guardian_consent_to_give_over_the_counter_medications',
        ),
    ]
