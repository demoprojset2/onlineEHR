# Generated by Django 4.0 on 2022-01-11 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_remove_doctordetails_uuid_doctordetails_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patientdetails',
            name='Doctor',
        ),
        migrations.AddField(
            model_name='patientdetails',
            name='doctor',
            field=models.ManyToManyField(blank=True, to='backend.DoctorDetails'),
        ),
    ]