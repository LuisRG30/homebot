# Generated by Django 3.1 on 2020-08-18 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeworkcrafter', '0024_auto_20200817_1825'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('email', models.CharField(max_length=64)),
                ('number', models.CharField(max_length=32)),
                ('level', models.CharField(default='bachillerato', max_length=32)),
                ('subject', models.CharField(max_length=64)),
                ('time', models.FloatField()),
                ('description', models.CharField(max_length=5000)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('paid', models.BooleanField(default=False)),
            ],
        ),
    ]
