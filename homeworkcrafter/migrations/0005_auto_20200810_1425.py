# Generated by Django 3.1 on 2020-08-10 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeworkcrafter', '0004_delivery'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delivery',
            name='delivery',
            field=models.FileField(upload_to=''),
        ),
    ]
