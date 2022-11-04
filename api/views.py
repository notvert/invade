from rest_framework import viewsets
from invadeapp.models import Champions, MatchData
from .serializers import ChampionSerializer, MatchDataSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter

class ChampionsViewSet(viewsets.ModelViewSet):
    queryset = Champions.objects.all() 
    serializer_class = ChampionSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ['hp', 'id', 'name', 'attackspeed', 'mp', 'attackdamage']
    ordering = ['name']

class MatchDataViewSet(viewsets.ModelViewSet):
    queryset = MatchData.objects.all() 
    serializer_class = MatchDataSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ['summoner_name_match', 'team_id', 'champion_id', 'spell1_id', 'spell2_id']
    ordering = ['summoner_name_match']