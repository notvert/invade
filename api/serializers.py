from rest_framework import serializers
from invadeapp.models import Champions, MatchData

class ChampionSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'key', 
            'name', 
            'attack',  
            'defense', 
            'magic',
            'difficulty', 
            'hp', 
            'hpperlevel', 
            'mp', 
            'mpperlevel', 
            'movespeed', 
            'armor', 
            'armorperlevel', 
            'spellblock', 
            'spellblockperlevel',
            'attackrange', 
            'hpregen', 
            'hpregenperlevel', 
            'mpregen', 
            'mpregenperlevel',
            'crit', 
            'critperlevel', 
            'attackdamage', 
            'attackdamageperlevel', 
            'attackspeedperlevel', 
            'attackspeed', 
            'image'
        )
        model = Champions

class MatchDataSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'summoner_name_match',
            'team_id', 
            'champion_id', 
            'spell1_id',
            'spell2_id'
        )
        model = MatchData
