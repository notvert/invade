from rest_framework import serializers
from invadeapp.models import Champions

class ChampionSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('number', 'name', 'height', 'weight', 'image_front', 'image_back', 'type_info', 'id')
        model = Champions
