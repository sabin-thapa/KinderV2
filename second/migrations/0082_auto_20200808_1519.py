# Generated by Django 3.0.7 on 2020-08-08 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('second', '0081_merge_20200808_1458'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignments',
            name='description',
            field=models.TextField(null=True),
        ),
    ]