# Generated by Django 5.0.1 on 2024-03-14 01:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0011_rename_lc_id_consup_master_lo_id'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Consup_detail',
            new_name='Consup_provider',
        ),
    ]