# Generated by Django 5.0.1 on 2024-02-05 17:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('providers', '0002_providers_pr_webacc'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActionTypes',
            fields=[
                ('at_id', models.AutoField(primary_key=True, serialize=False)),
                ('at_name', models.CharField(max_length=50)),
                ('at_desc', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ActionsMaster',
            fields=[
                ('am_id', models.AutoField(primary_key=True, serialize=False)),
                ('am_name', models.CharField(max_length=50)),
                ('am_desc', models.CharField(max_length=200)),
                ('pr_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='providers.providers')),
            ],
        ),
        migrations.CreateModel(
            name='ActionsDetail',
            fields=[
                ('ad_id', models.AutoField(primary_key=True, serialize=False)),
                ('ad_seq', models.IntegerField()),
                ('am_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='providers.actionsmaster')),
                ('ad_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='providers.actiontypes')),
            ],
        ),
    ]