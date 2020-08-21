# Generated by Django 3.1 on 2020-08-18 18:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homeworkcrafter', '0025_video'),
    ]

    operations = [
        migrations.CreateModel(
            name='Express',
            fields=[
                ('homework_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='homeworkcrafter.homework')),
            ],
            bases=('homeworkcrafter.homework',),
        ),
        migrations.DeleteModel(
            name='Video',
        ),
    ]