# Generated by Django 3.0.4 on 2020-03-11 10:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('announcement', '0002_announcement'),
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, upload_to='default/')),
                ('announcement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='announcement.Announcement')),
            ],
        ),
    ]
