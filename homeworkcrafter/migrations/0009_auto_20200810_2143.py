# Generated by Django 3.1 on 2020-08-11 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeworkcrafter', '0008_auto_20200810_2139'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='delivery',
            name='code',
        ),
        migrations.AddField(
            model_name='homework',
            name='code',
            field=models.CharField(default='', max_length=16),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='homework',
            name='done',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='homework',
            name='price',
            field=models.IntegerField(blank=True),
        ),
    ]
