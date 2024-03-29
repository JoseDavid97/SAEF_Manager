# Generated by Django 5.0.1 on 2024-03-14 01:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('locations', '0006_locations_pr_name_locations_pr_webacc'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meters',
            fields=[
                ('mt_id', models.AutoField(primary_key=True, serialize=False)),
                ('mt_name', models.CharField(max_length=100)),
                ('lo_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='locations.locations')),
            ],
        ),
    ]
