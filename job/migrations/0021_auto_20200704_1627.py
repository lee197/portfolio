# Generated by Django 3.0.8 on 2020-07-04 16:27

from django.db import migrations
import s3direct.fields


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0020_auto_20200704_1625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='main_image',
            field=s3direct.fields.S3DirectField(blank=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='personal_image',
            field=s3direct.fields.S3DirectField(blank=True),
        ),
    ]
