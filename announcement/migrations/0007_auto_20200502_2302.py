# Generated by Django 3.0.4 on 2020-05-02 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('announcement', '0006_auto_20200430_1658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='comment',
            name='subject',
            field=models.CharField(max_length=50),
        ),
    ]