# Generated by Django 5.0.1 on 2024-02-06 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('providers', '0005_remove_providers_pr_webacc'),
    ]

    operations = [
        migrations.AddField(
            model_name='providers',
            name='pr_webacc',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]