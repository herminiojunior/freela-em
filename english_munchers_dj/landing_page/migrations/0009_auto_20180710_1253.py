# Generated by Django 2.0 on 2018-07-10 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing_page', '0008_auto_20180709_2321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classinfo',
            name='class_length',
            field=models.CharField(blank=True, default='', max_length=128, null=True),
        ),
    ]