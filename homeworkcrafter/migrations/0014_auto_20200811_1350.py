# Generated by Django 3.1 on 2020-08-11 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeworkcrafter', '0013_homework_erase'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homework',
            name='erase',
        ),
        migrations.AddField(
            model_name='delivery',
            name='erase',
            field=models.BooleanField(default=False),
        ),
    ]