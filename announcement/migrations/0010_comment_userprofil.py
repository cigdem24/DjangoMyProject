# Generated by Django 3.0.4 on 2020-05-08 12:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_userprofile'),
        ('announcement', '0009_auto_20200507_1625'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='userprofil',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='home.UserProfile'),
            preserve_default=False,
        ),
    ]
