from django.urls import path
from . import views

app_name = 'invadeapp'

urlpatterns = [
    path("", views.index, name="index"),
    path("champions/", views.champions, name="champions"),
    path("savename/", views.savename, name='savename')
    # path("champions_hp/", views.sortByHp, name="sortByHp"),
    # path("champions_mp/", views.sortByMp, name="sortByMp"),
    # path("champions_crit/", views.sortByCrit, name="sortByCrit"),
    # path("champions_attackdamage/", views.sortByAttackdamage, name="sortByAttackdamage"),
    # path("<str:attribute>/", views.sortByAttribute, name="sortByAttribute"),
]