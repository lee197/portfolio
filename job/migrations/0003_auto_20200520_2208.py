# Generated by Django 3.0.6 on 2020-05-20 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0002_advices_works'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advices',
            name='description',
            field=models.CharField(default='fudi', max_length=500),
        ),
        migrations.AlterField(
            model_name='advices',
            name='name',
            field=models.CharField(default='fudi', max_length=50),
        ),
        migrations.AlterField(
            model_name='works',
            name='image_name',
            field=models.CharField(default='fudi', max_length=50),
        ),
        migrations.AlterField(
            model_name='works',
            name='name',
            field=models.CharField(default='fudi', max_length=50),
        ),
        migrations.AlterField(
            model_name='works',
            name='type',
            field=models.CharField(default='iOS', max_length=50),
        ),
    ]
