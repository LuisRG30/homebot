# Generated by Django 3.1 on 2020-08-12 02:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homeworkcrafter', '0017_auto_20200811_2132'),
        ('staff', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='job',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='worker', to='homeworkcrafter.homework'),
        ),
    ]
