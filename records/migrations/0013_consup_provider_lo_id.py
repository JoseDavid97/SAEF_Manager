# Generated by Django 5.0.1 on 2024-03-14 01:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0006_locations_pr_name_locations_pr_webacc'),
        ('records', '0012_rename_consup_detail_consup_provider'),
    ]

    operations = [
        migrations.AddField(
            model_name='consup_provider',
            name='lo_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='locations.locations'),
            preserve_default=False,
        ),
    ]
