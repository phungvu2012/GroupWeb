# Generated by Django 3.0.11 on 2020-11-26 05:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0006_auto_20201126_1204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grouphasaccount',
            name='userName',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]