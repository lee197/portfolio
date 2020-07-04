# Generated by Django 3.0.8 on 2020-07-04 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0021_auto_20200704_1627'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='main_image_name',
        ),
        migrations.RemoveField(
            model_name='person',
            name='personal_image_name',
        ),
        migrations.RemoveField(
            model_name='project',
            name='image_name',
        ),
        migrations.RemoveField(
            model_name='works',
            name='work_image_name',
        ),
        migrations.RemoveField(
            model_name='works',
            name='work_image_url',
        ),
        migrations.AddField(
            model_name='project',
            name='project_image',
            field=models.ImageField(default='img/0.jpg', upload_to='img/'),
        ),
        migrations.AlterField(
            model_name='person',
            name='main_image',
            field=models.ImageField(default='img/0.jpg', upload_to='img/'),
        ),
        migrations.AlterField(
            model_name='person',
            name='personal_image',
            field=models.ImageField(default='img/0.jpg', upload_to='img/'),
        ),
    ]