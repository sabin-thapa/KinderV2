# Generated by Django 2.2.7 on 2020-07-31 08:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('second', '0063_auto_20200731_1214'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attachment',
            old_name='subject',
            new_name='course',
        ),
        migrations.RenameField(
            model_name='tutorial',
            old_name='subject',
            new_name='course',
        ),
    ]
