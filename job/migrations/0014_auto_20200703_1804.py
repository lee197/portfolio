# Generated by Django 3.0.7 on 2020-07-03 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0013_auto_20200703_1647'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='image_name',
            field=models.CharField(default='Lee', max_length=500),
        ),
        migrations.AddField(
            model_name='project',
            name='title',
            field=models.CharField(default="Lee's project", max_length=50),
        ),
    ]
