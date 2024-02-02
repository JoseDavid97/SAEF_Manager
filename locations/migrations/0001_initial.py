# Generated by Django 4.2.9 on 2024-01-27 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Countries',
            fields=[
                ('co_iso_num', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('co_iso_al2', models.CharField(max_length=2)),
                ('co_iso_al3', models.CharField(max_length=3)),
                ('co_call_code', models.CharField(max_length=5)),
                ('co_name', models.CharField(max_length=50)),
            ],
        ),
    ]
