from django.urls import path
from . import views

app_name = 'invadeapp'

urlpatterns = [
    path("", views.index, name="index"),
    path("champions/", views.champions, name="champions"),
    path("champions_hp/", views.sortByHp, name="sortByHp"),
    path("<str:attribute>/", views.sortByAttribute, name="sortByAttribute"),
]