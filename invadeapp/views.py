from django.shortcuts import redirect, render
from django.http import JsonResponse
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
    key = "RGAPI-ff391a2a-c65c-4ffc-bd80-446a6973d993"
    url = "https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + summoner_name + "?api_key=" + key
    payload = ""
    headers = {
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.text)
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
    print(transform)
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
    
        # for loop through object, determine what team each person is in, 
        # what their champion HP is, add their HP to team's total,
        # compare the two numbers, and return "invade = yes" if your team (100)
        # redirect to another page, display this information
        # matchrecord = MatchData(game_id=game_id, map_id=map_id)
        # matchrecord.save()
    except KeyError: 
        print("Player offline")


    return redirect("/")
