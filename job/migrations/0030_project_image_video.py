# Generated by Django 3.0.8 on 2020-07-06 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0029_project_is_screen'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='image_video',
            field=models.ImageField(default='img/0.jpg', upload_to='img/'),
        ),
    ]