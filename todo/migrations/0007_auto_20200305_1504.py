# Generated by Django 3.0.2 on 2020-03-05 20:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0006_auto_20200302_1233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='due_date',
            field=models.DateField(default=datetime.datetime(2020, 3, 5, 15, 4, 33, 555410)),
        ),
    ]