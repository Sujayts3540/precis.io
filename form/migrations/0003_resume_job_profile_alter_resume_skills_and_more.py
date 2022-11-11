# Generated by Django 4.1.1 on 2022-11-11 06:15

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0002_resume_uid'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='job_profile',
            field=models.CharField(blank=True, max_length=12),
        ),
        migrations.AlterField(
            model_name='resume',
            name='skills',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=20), size=None),
        ),
        migrations.AlterField(
            model_name='resume',
            name='website',
            field=models.URLField(blank=True),
        ),
    ]
