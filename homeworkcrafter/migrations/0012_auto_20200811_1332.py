# Generated by Django 3.1 on 2020-08-11 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeworkcrafter', '0011_homework_paid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homework',
            name='code',
            field=models.CharField(max_length=16, unique=True),
        ),
    ]
