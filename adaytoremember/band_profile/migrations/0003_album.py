# Generated by Django 2.2.5 on 2019-09-23 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('band_profile', '0002_delete_album'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
