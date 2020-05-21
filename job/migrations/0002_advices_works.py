# Generated by Django 3.0.6 on 2020-05-20 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Advices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='fudi', max_length=20)),
                ('description', models.CharField(default='fudi', max_length=20)),
                ('rank', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Works',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='fudi', max_length=20)),
                ('image_name', models.CharField(default='fudi', max_length=20)),
                ('type', models.CharField(default='iOS', max_length=20)),
            ],
        ),
    ]