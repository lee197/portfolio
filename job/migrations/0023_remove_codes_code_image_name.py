# Generated by Django 3.0.8 on 2020-07-04 17:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0022_auto_20200704_1702'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='codes',
            name='code_image_name',
        ),
    ]