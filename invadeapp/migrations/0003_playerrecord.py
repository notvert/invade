# Generated by Django 4.1 on 2022-10-27 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invadeapp', '0002_champions_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlayerRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('summoner_name', models.CharField(max_length=100)),
                ('eid', models.CharField(max_length=200)),
            ],
        ),
    ]
