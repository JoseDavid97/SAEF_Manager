# Generated by Django 5.0.1 on 2024-02-12 21:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0006_consup_detail_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='consup_detail',
            old_name='cd',
            new_name='cd_id',
        ),
        migrations.AddField(
            model_name='consup_detail',
            name='cm_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='records.consup_master'),
            preserve_default=False,
        ),
    ]
