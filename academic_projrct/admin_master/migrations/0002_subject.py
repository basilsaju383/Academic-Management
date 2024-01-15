# Generated by Django 5.0 on 2024-01-15 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_master', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_name', models.CharField(max_length=200)),
                ('status', models.IntegerField(default=1)),
                ('classes', models.ManyToManyField(to='admin_master.masterclass')),
            ],
        ),
    ]
