# Generated by Django 5.0.1 on 2024-02-11 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0004_alter_providerconsuptions_pc_kvarhc_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='providerconsuptions',
            name='pc_kWh',
            field=models.DecimalField(decimal_places=2, max_digits=7, null=True),
        ),
    ]
