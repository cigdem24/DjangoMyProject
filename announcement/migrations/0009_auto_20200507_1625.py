# Generated by Django 3.0.4 on 2020-05-07 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('announcement', '0008_auto_20200503_1752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='rate',
            field=models.IntegerField(),
        ),
    ]
