# Generated by Django 3.0.6 on 2020-05-16 22:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20200509_2055'),
        ('announcement', '0017_remove_announcement_userprofil'),
    ]

    operations = [
        migrations.AddField(
            model_name='announcement',
            name='profile',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='home.UserProfile'),
            preserve_default=False,
        ),
    ]
