# Generated by Django 3.0.4 on 2020-05-03 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('announcement', '0007_auto_20200502_2302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
