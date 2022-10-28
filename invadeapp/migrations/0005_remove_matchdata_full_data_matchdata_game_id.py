# Generated by Django 4.1 on 2022-10-28 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invadeapp', '0004_matchdata_alter_playerrecord_eid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='matchdata',
            name='full_data',
        ),
        migrations.AddField(
            model_name='matchdata',
            name='game_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]