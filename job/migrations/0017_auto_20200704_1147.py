# Generated by Django 3.0.7 on 2020-07-04 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0016_projectimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectimage',
            name='image_name',
        ),
        migrations.AddField(
            model_name='projectimage',
            name='big_image_name',
            field=models.CharField(default='Lee', max_length=20),
        ),
        migrations.AddField(
            model_name='projectimage',
            name='small_image_name',
            field=models.CharField(default='Lee', max_length=20),
        ),
        migrations.AddField(
            model_name='projectimage',
            name='title',
            field=models.CharField(default='Lee', max_length=50),
        ),
    ]
