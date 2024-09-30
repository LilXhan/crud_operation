# Generated by Django 5.0.9 on 2024-09-29 13:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pay_roll_app', '0005_rename_dept_name_department_department_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='employee_country',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, related_name='Country', to='pay_roll_app.country'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='employee_department',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, related_name='Deparment', to='pay_roll_app.department'),
        ),
    ]