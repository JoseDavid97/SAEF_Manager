# Generated by Django 4.2.9 on 2024-01-27 22:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0004_location'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Location',
            new_name='Locations',
        ),
    ]