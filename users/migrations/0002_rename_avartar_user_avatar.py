# Generated by Django 4.2.2 on 2023-06-28 04:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='avartar',
            new_name='avatar',
        ),
    ]