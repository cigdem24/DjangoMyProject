# Generated by Django 3.0.4 on 2020-05-13 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0004_content_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='type',
            field=models.CharField(choices=[('menu', 'menu'), ('duyuru', 'duyuru')], max_length=10),
        ),
    ]
