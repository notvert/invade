from rest_framework import viewsets
from invadeapp.models import Champions
from .serializers import ChampionSerializer

class ChampionsViewSet(viewsets.ModelViewSet):
    queryset = Champions.objects.all()
    serializer_class = ChampionSerializer
   