# Generated by Django 3.0.6 on 2020-05-16 22:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('announcement', '0015_auto_20200517_0034'),
    ]

    operations = [
        migrations.RenameField(
            model_name='announcement',
            old_name='profile',
            new_name='userprofil',
        ),
    ]
