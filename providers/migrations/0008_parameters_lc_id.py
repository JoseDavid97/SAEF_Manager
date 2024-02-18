# Generated by Django 5.0.1 on 2024-02-18 16:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0006_locations_pr_name_locations_pr_webacc'),
        ('providers', '0007_parameters'),
    ]

    operations = [
        migrations.AddField(
            model_name='parameters',
            name='lc_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='locations.locations'),
        ),
    ]
