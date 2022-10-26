from riotwatcher import LolWatcher, ApiError
import json

# golbal variables

x = input('Enter your summoner name:')

api_key = 'RGAPI-64e1bebd-4568-46f6-a182-81e92d150d4c'
watcher = LolWatcher(api_key)
my_region = 'na1'

me = watcher.summoner.by_name(my_region, x)

print(me)