# Generated by Django 3.0.3 on 2020-02-16 16:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meetings', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Meetings',
            new_name='Meeting',
        ),
    ]
