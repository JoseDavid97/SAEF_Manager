# Generated by Django 5.0.3 on 2024-03-17 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parameters', '0003_remove_parameters_par_value_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='parameters',
            name='par_value_string',
        ),
        migrations.AddField(
            model_name='parameters',
            name='par_value',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
