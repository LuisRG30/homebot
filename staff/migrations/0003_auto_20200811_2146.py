# Generated by Django 3.1 on 2020-08-12 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeworkcrafter', '0017_auto_20200811_2132'),
        ('staff', '0002_auto_20200811_2138'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='job',
        ),
        migrations.AddField(
            model_name='profile',
            name='job',
            field=models.ManyToManyField(blank=True, null=True, related_name='worker', to='homeworkcrafter.Homework'),
        ),
    ]
