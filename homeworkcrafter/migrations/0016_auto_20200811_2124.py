# Generated by Django 3.1 on 2020-08-12 02:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homeworkcrafter', '0015_remove_delivery_erase'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delivery',
            name='homework',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='assignments', serialize=False, to='homeworkcrafter.homework'),
        ),
    ]
