# Generated by Django 3.0.7 on 2020-08-08 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('second', '0076_auto_20200808_1102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignments',
            name='deadline',
            field=models.DateField(blank=True),
        ),
    ]
