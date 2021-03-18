# Generated by Django 3.1.7 on 2021-03-18 08:07

import activity.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('name', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=100)),
                ('photo', models.FileField(upload_to='', validators=[activity.validators.validate_file_extension])),
                ('start_time', models.DateTimeField()),
                ('duration', models.FloatField()),
                ('normal_price', models.FloatField()),
                ('member_price', models.FloatField()),
                ('number_participants', models.IntegerField()),
                ('status', models.CharField(choices=[('P', 'Pending'), ('C', 'Cancelled'), ('D', 'Done')], max_length=20)),
                ('location', models.CharField(max_length=20)),
                ('only_member', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'Activities',
            },
        ),
    ]
