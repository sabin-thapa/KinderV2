# Generated by Django 3.0.8 on 2020-08-08 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('second', '0072_auto_20200808_1944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='announcement',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='course_plan',
            field=models.FileField(blank=True, null=True, upload_to='course_plan/', verbose_name='Course Plan'),
        ),
    ]
