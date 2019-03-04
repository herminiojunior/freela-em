# Generated by Django 2.0 on 2019-03-04 16:52

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing_page', '0010_auto_20180716_1142'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('config', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=(('15', '15 minutes'), ('30', '30 minutes'), ('45', '45 minutes'), ('60', '60 minutes'), ('open', 'Open Time')), null=True)),
            ],
        ),
    ]
