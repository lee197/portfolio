# Generated by Django 3.0.6 on 2020-05-20 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0003_auto_20200520_2208'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='works',
            name='image_name',
        ),
        migrations.AddField(
            model_name='works',
            name='work_image',
            field=models.ImageField(default='images/0.jpg', upload_to='images/'),
        ),
    ]
