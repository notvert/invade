# Generated by Django 4.1 on 2022-11-01 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invadeapp', '0006_matchdata_map_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='matchdata',
            name='map_id',
        ),
        migrations.AddField(
            model_name='matchdata',
            name='champion_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='matchdata',
            name='spell1_id',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
        migrations.AddField(
            model_name='matchdata',
            name='spell2_id',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
        migrations.AddField(
            model_name='matchdata',
            name='summonerName',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
