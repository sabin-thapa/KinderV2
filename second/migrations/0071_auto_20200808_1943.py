# Generated by Django 3.0.8 on 2020-08-08 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('second', '0070_merge_20200808_1943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_plan',
            field=models.FileField(null=True, upload_to='course_plan/', verbose_name='Course Plan'),
        ),
        migrations.AlterField(
            model_name='course',
            name='syllabus',
            field=models.FileField(blank=True, null=True, upload_to='syllabus/', verbose_name='Syallabus'),
        ),
    ]