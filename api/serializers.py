from rest_framework import serializers
from invadeapp.models import Champions

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


