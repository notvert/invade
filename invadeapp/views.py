from django.shortcuts import redirect, render
from django.http import JsonResponse, HttpResponse
from .models import Champions, PlayerRecord, MatchData
from rest_framework import status
from rest_framework.response import Response
from django.core.management import call_command
import requests
import json

def index(request):
    return render(request, 'invadeapp/index.html')

def champions(request):
    champion = list(Champions.objects.all().values())
    return JsonResponse(champion,
        safe=False, status=status.HTTP_200_OK)

def savename(request): # a view for receiving a form submission
    # print(request.POST) # verify we received the form data
    summoner_name = request.POST['summonerName'] # get the value the user entered
    # print(summoner_name)
    key = "RGAPI-f9f99b6a-db56-4689-a639-438b3c189c37"
    url = "https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + summoner_name + "?api_key=" + key
    payload = ""
    headers = {
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    # print(response.text)
    results = json.loads(response.text)
    # print(results)
    eid = results["id"]
    # print(eid)
    playerrecord = PlayerRecord(summoner_name=summoner_name, eid=eid) # create an instance of our model
    playerrecord.save() # save a new row to the database
    url2 = "https://na1.api.riotgames.com/lol/spectator/v4/active-games/by-summoner/" + eid + "?api_key=" + key
    payload2 = ""
    headers2 = {
    }
    response2 = requests.request("GET", url2, headers=headers2, data=payload2)
    # print(response2.text)
    transform = json.loads(response2.text)
    # print(transform)
    # print(transform["gameId"])

    try:
        # print("Connection successful")
        # game_id = transform["gameId"]
        # map_id = transform["mapId"]
        # print(game_id)
        with open("sample.json","w") as player: 
            json.dump(transform,player)
        call_command("load_match")
        team_1_data = 0
        team_2_data = 0
        match = MatchData.objects.all()
        champ = Champions.objects.all()

        for summoner in match:
            # print(summoner.champion_id)

            for c in champ:

                if c.key == int(summoner.champion_id) and int(summoner.team_id) == 100:
                    # print(c.hp)
                    team_1_data = team_1_data + c.hp
                    # print(team_1_data)
                    
                elif c.key == int(summoner.champion_id) and int(summoner.team_id) == 200:
                        # print(c.hp)
                    team_2_data = team_2_data + c.hp
                    # print(team_2_data)

        if team_1_data > team_2_data:
            print("team 1 data:" + str(team_1_data))
            print("team 2 data:" + str(team_2_data))
            return HttpResponse("invade")
            

        else:
            return HttpResponse("don't invade")

    except KeyError: 
        print("Player offline")

    return redirect("/")


def match(request):
    summoner = list(MatchData.objects.all().values())
    return JsonResponse(summoner,
        safe=False, status=status.HTTP_200_OK)

