# Generated by Django 2.2.7 on 2020-07-31 14:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('second', '0065_auto_20200731_1953'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='announcemt',
            new_name='announcement',
        ),
    ]
