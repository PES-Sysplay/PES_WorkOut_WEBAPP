# Generated by Django 3.1.7 on 2021-03-20 15:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='activity',
            unique_together={('activity_type', 'start_date', 'start_time', 'location')},
        ),
    ]