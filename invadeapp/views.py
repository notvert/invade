from django.shortcuts import redirect, render
from django.http import JsonResponse
from .models import Champions, PlayerRecord, MatchData
from rest_framework import status
from rest_framework.response import Response
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
    key = "RGAPI-b9cbeec8-e5da-44e7-8d4c-17dde8508af5"
    url = "https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + summoner_name + "?api_key=" + key
    payload = ""
    headers = {
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    # print(response.text)
    id = json.loads(response.text)
    eid = id["id"]
    # print(eid)
    url2 = "https://na1.api.riotgames.com/lol/spectator/v4/active-games/by-summoner/" + eid + "?api_key=" + key
    payload2 = ""
    headers2 = {
    }
    response2 = requests.request("GET", url2, headers=headers2, data=payload2)
    # print(response2.text)
    transform = json.loads(response2.text)
    game_id = transform["gameId"]
    map_id = transform["mapId"]
    # print(game_id)
    print(game_id)
    matchrecord = MatchData(game_id=game_id, map_id=map_id)
    matchrecord.save()
    # https://docs.djangoproject.com/en/4.1/ref/models/querysets/ if the summoner name exists, don't add it again
    playerrecord = PlayerRecord(summoner_name=summoner_name, eid=eid) # create an instance of our model
    playerrecord.save() # save a new row to the database
    return redirect("/")


# def sortByHp(request):
#     champions_sorted = list(Champions.objects.all().order_by('-hp').values())[0:10]
#     return JsonResponse(champions_sorted,
#         safe=False, status=status.HTTP_200_OK)

# def sortByMp(request):
#     champions_sorted = list(Champions.objects.all().order_by('-mp').values())[0:10]
#     return JsonResponse(champions_sorted,
#         safe=False, status=status.HTTP_200_OK)

# def sortByCrit(request):
#     champions_sorted = list(Champions.objects.all().order_by('-crit').values())[0:10]
#     return JsonResponse(champions_sorted,
#         safe=False, status=status.HTTP_200_OK)

# def sortByAttackdamage(request):
#     champions_sorted = list(Champions.objects.all().order_by('-attackdamage').values())[0:10]
#     return JsonResponse(champions_sorted,
#         safe=False, status=status.HTTP_200_OK)


# def sortByAttribute(request, attribute):
#     attribute_value = request.POST.get('attribute', None)
#     attribute = '-' + attribute_value
#     champions_sorted = list(Champions.objects.all().order_by(attribute).values())
#     return JsonResponse(champions_sorted,
#         safe=False, status=status.HTTP_200_OK)