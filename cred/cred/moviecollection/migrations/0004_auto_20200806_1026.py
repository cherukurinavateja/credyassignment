# Generated by Django 3.0.8 on 2020-08-06 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviecollection', '0003_auto_20200806_1022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moviecollections',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='moviecollections',
            name='title',
            field=models.CharField(default='', max_length=100),
        ),
    ]
