from rest_framework import viewsets
from invadeapp.models import Champions
from .serializers import ChampionSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter

class ChampionsViewSet(viewsets.ModelViewSet):
    queryset = Champions.objects.all() 
    serializer_class = ChampionSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ['hp', 'id', 'name', 'attackspeed', 'mp', 'attackdamage']
    ordering = ['name']