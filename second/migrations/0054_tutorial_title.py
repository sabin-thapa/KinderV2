# Generated by Django 2.2.7 on 2020-07-30 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('second', '0053_tutorial_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutorial',
            name='title',
            field=models.TextField(null=True),
        ),
    ]
