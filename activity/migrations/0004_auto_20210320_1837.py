# Generated by Django 3.1.7 on 2021-03-20 17:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0003_auto_20210320_1631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='description',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='activity',
            name='location',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='activity',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='activity',
            name='start_date',
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='activity',
            name='start_time',
            field=models.TimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='activity',
            name='status',
            field=models.CharField(choices=[('P', 'Pendiente'), ('C', 'Cancelada'), ('D', 'Finalizada')], default='P', max_length=1),
        ),
        migrations.AlterField(
            model_name='activitytype',
            name='name',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]