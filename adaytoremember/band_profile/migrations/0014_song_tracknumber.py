# Generated by Django 2.2.5 on 2019-09-23 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('band_profile', '0013_auto_20190923_1850'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='trackNumber',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
