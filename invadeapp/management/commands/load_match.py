from django.core.management.base import BaseCommand
from invadeapp.models import MatchData
import json

class Command(BaseCommand):

    def handle(self, *args, **options):
        MatchData.objects.all().delete()
        f = open('sample.json')
        match_data = json.load(f)
        # match_data2 = match_data["participants"]
        # print(match_data2)
        # print(match_data["participants"][0]["championId"])

        for match in match_data["participants"]:
            print(match["summonerName"])
            summoner_name_ext = match["summonerName"]
            champion_id_ext = match["championId"]
            team_id_ext = match["teamId"]
            spell1Id_ext = match["spell1Id"]
            spell2Id_ext = match["spell2Id"]

            MatchData.objects.create(
                summoner_name_match = summoner_name_ext,
                team_id = team_id_ext,
                champion_id = champion_id_ext,
                spell1_id = spell1Id_ext,
                spell2_id  = spell2Id_ext,
            )            
                