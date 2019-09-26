# Generated by Django 2.2.5 on 2019-09-23 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='BandMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first', models.CharField(max_length=64)),
                ('last', models.CharField(max_length=64)),
                ('instrument', models.CharField(choices=[('LV', 'Lead Vocals'), ('RG', 'Rhythm Guitar'), ('BG', 'Bass Guitar'), ('D', 'Drums'), ('LG', 'Lead Guitar')], max_length=64)),
                ('years_in_band', models.CharField(max_length=64)),
                ('hometown', models.CharField(max_length=64)),
            ],
        ),
    ]
