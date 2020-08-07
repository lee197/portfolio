# Generated by Django 3.0.8 on 2020-07-04 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0023_remove_codes_code_image_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectimage',
            name='big_image_name',
        ),
        migrations.RemoveField(
            model_name='projectimage',
            name='small_image_name',
        ),
        migrations.AddField(
            model_name='projectimage',
            name='big_image',
            field=models.ImageField(default='img/0.jpg', upload_to='img/'),
        ),
        migrations.AddField(
            model_name='projectimage',
            name='main_image',
            field=models.ImageField(default='img/0.jpg', upload_to='img/'),
        ),
        migrations.AddField(
            model_name='projectimage',
            name='small_image',
            field=models.ImageField(default='img/0.jpg', upload_to='img/'),
        ),
        migrations.AddField(
            model_name='projectimage',
            name='subtitle',
            field=models.CharField(default='Lee', max_length=200),
        ),
        migrations.AddField(
            model_name='projectimage',
            name='video_link',
            field=models.CharField(default='Lee', max_length=50),
        ),
        migrations.AlterField(
            model_name='projectimage',
            name='summary',
            field=models.TextField(default='Lee', max_length=500),
        ),
    ]
