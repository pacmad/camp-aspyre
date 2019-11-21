# Generated by Django 2.2.7 on 2019-11-21 22:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MedicalInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('height', models.CharField(max_length=255)),
                ('weight', models.IntegerField()),
                ('biological_sex', models.CharField(max_length=255)),
                ('full_address', models.CharField(max_length=255)),
                ('emergency_contact', models.CharField(max_length=255)),
                ('relationship_to_student', models.CharField(max_length=255)),
                ('best_phone_number_during_camp', models.CharField(max_length=255)),
                ('best_phone_number_during_camp_secondary', models.CharField(max_length=255)),
                ('alternate_contact', models.CharField(max_length=255)),
                ('doctor_name', models.CharField(max_length=255)),
                ('doctor_phone', models.CharField(max_length=255)),
                ('doctor_address', models.CharField(max_length=255)),
                ('health_insurance_name', models.CharField(max_length=255)),
                ('insurance_policy_number', models.CharField(max_length=255)),
                ('other_pertinent_insurance_info', models.CharField(max_length=255)),
                ('taking_meds', models.BooleanField()),
                ('nervousness', models.BooleanField()),
                ('mental_disorder', models.BooleanField()),
                ('convulsions_epilepsy', models.BooleanField()),
                ('fainting', models.BooleanField()),
                ('heart_condition', models.BooleanField()),
                ('rheumatic_fever', models.BooleanField()),
                ('cancer_tumor', models.BooleanField()),
                ('high_blood_pressure', models.BooleanField()),
                ('headaches', models.BooleanField()),
                ('asthma', models.BooleanField()),
                ('ulcers', models.BooleanField()),
                ('diabetes', models.BooleanField()),
                ('medication_allergies', models.BooleanField()),
                ('other_allergies_illnesses', models.BooleanField()),
                ('physical_limitations', models.CharField(max_length=255)),
                ('details_answers', models.CharField(max_length=255)),
                ('camper', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Camper')),
                ('registration', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Registration')),
            ],
        ),
    ]