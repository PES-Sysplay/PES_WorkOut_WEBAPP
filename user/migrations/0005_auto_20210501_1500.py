# Generated by Django 3.1.7 on 2021-05-01 13:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20210421_1527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organizer',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.organization'),
        ),
    ]
