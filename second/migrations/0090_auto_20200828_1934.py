# Generated by Django 2.2.7 on 2020-08-28 13:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('second', '0089_auto_20200828_0855'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Attendance',
        ),
        migrations.DeleteModel(
            name='Food',
        ),
        migrations.DeleteModel(
            name='StudentId',
        ),
    ]
