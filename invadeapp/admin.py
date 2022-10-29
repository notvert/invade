from django.contrib import admin
from .models import Champions, PlayerRecord, MatchData, AllData

admin.site.register(Champions)
admin.site.register(PlayerRecord)
admin.site.register(MatchData)
admin.site.register(AllData)