# Generated by Django 2.0 on 2018-10-06 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('link', models.CharField(max_length=100)),
                ('size', models.IntegerField()),
                ('filetype', models.CharField(max_length=5)),
                ('deletehash', models.CharField(max_length=100)),
            ],
        ),
    ]
