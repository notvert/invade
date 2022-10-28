from django.contrib import admin
from .models import Champions, PlayerRecord, MatchData

admin.site.register(Champions)
admin.site.register(PlayerRecord)
admin.site.register(MatchData)