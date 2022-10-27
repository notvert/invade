from django.shortcuts import render
from django.http import JsonResponse, HttpResponseRedirect
from .models import Champions, PlayerRecord
from django.core import serializers
from rest_framework import status
from rest_framework.response import Response

def index(request):
    return render(request, 'invadeapp/index.html')

def champions(request):
    champion = list(Champions.objects.all().values())
    return JsonResponse(champion,
        safe=False, status=status.HTTP_200_OK)

def savename(request): # a view for receiving a form submission
    print(request.POST) # verify we received the form data
    summoner_name = request.POST['summonerName'] # get the value the user entered
    playerrecord = PlayerRecord(summoner_name=summoner_name) # create an instance of our model
    playerrecord.save() # save a new row to the database
    return render(request, 'invadeapp/index.html')




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