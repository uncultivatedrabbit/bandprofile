# Generated by Django 2.2.5 on 2019-09-23 22:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('band_profile', '0004_auto_20190923_1819'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Record',
            new_name='Album',
        ),
    ]
