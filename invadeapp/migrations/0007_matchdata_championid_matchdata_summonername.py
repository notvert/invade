# Generated by Django 4.1 on 2022-10-29 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invadeapp', '0006_matchdata_map_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='matchdata',
            name='championId',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='matchdata',
            name='summonerName',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
