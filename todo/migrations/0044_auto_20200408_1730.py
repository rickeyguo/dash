# Generated by Django 3.0.3 on 2020-04-08 17:30

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('todo', '0043_auto_20200408_1432'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='todo',
            name='due_date',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]
