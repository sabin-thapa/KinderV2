# Generated by Django 2.2.7 on 2020-07-31 14:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('second', '0064_auto_20200731_1444'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='announcement',
        ),
        migrations.AddField(
            model_name='attachment',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='course',
            name='announcemt',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='tutorial',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
