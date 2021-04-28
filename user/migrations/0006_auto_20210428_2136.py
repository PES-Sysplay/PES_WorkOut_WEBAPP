# Generated by Django 3.1.7 on 2021-04-28 19:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_favorites'),
    ]

    operations = [
        migrations.RenameField(
            model_name='favorites',
            old_name='user',
            new_name='client',
        ),
        migrations.AlterUniqueTogether(
            name='favorites',
            unique_together={('client', 'organization')},
        ),
    ]
