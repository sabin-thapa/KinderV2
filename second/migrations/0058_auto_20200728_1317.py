# Generated by Django 3.0.7 on 2020-07-28 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('second', '0057_auto_20200728_1314'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assignments',
            name='author',
        ),
        migrations.AddField(
            model_name='assignments',
            name='deadline',
            field=models.DateField(auto_now=True),
        ),
    ]
