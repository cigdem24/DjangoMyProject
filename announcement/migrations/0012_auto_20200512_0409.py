# Generated by Django 3.0.4 on 2020-05-12 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('announcement', '0011_auto_20200512_0352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='rate',
            field=models.IntegerField(),
        ),
    ]