# Generated by Django 3.0.7 on 2020-07-28 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('second', '0061_remove_assignments_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignments',
            name='file',
            field=models.FileField(blank=True, upload_to='assignments/', verbose_name=''),
        ),
    ]
