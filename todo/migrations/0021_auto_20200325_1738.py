# Generated by Django 3.0.2 on 2020-03-25 21:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0020_auto_20200314_0556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='due_date',
            field=models.DateField(default=datetime.datetime(2020, 3, 25, 17, 38, 27, 906295)),
        ),
    ]
