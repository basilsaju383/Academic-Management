# Generated by Django 5.0 on 2024-01-16 11:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_employee', '0002_department_employee_employeedesignation_empsalary'),
        ('admin_master', '0002_subject'),
    ]

    operations = [
        migrations.CreateModel(
            name='sub_cls_div',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_master.masterclass')),
                ('divid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_master.masterdivision')),
                ('empid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_employee.employeeregistration')),
                ('subid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_master.subject')),
            ],
        ),
    ]