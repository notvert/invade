# Generated by Django 4.1 on 2022-10-28 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invadeapp', '0005_remove_matchdata_full_data_matchdata_game_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='matchdata',
            name='map_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]