# Generated by Django 3.0.2 on 2020-03-07 01:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('grades', '0010_remove_assignment_grade_percentage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='ass_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grades.assType'),
        ),
    ]
