from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import ChampionsViewSet

router = DefaultRouter()
router.register('champions', ChampionsViewSet, basename='champions'),

urlpatterns = router.urls + [

]