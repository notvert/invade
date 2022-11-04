from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import ChampionsViewSet, MatchDataViewSet

router = DefaultRouter()
router.register('champions', ChampionsViewSet, basename='champions'),
router.register('match', MatchDataViewSet, basename='match'),

urlpatterns = router.urls + [
]