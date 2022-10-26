from riotwatcher import LolWatcher, ApiError
import json

# golbal variables
api_key = 'RGAPI-64e1bebd-4568-46f6-a182-81e92d150d4c'
watcher = LolWatcher(api_key)
my_region = 'na1'

me = watcher.summoner.by_name(my_region, 'notvert')

print(me)

# # all objects are returned (by default) as a dict
# # lets see if i got diamond yet (i probably didnt)
# my_ranked_stats = watcher.league.by_summoner(my_region, me['id'])
# print(my_ranked_stats)

# # First we get the latest version of the game from data dragon
# versions = watcher.data_dragon.versions_for_region(my_region)
# champions_version = versions['n']['champion']

# Lets get some champions


# current_champ_list = watcher.data_dragon.champions(champions_version)
# print(current_champ_list['data'])

# data = current_champ_list['data']
# for d in data: 
#     print(data[d])

# data_json = json.dumps(data)
# print(data_json)


# grab d and pass it through key value 

# print(current_champ_list['data'].keys())



# For Riot's API, the 404 status code indicates that the requested data wasn't found and
# should be expected to occur in normal operation, as in the case of a an
# invalid summoner name, match ID, etc.
#
# The 429 status code indicates that the user has sent too many requests
# in a given amount of time ("rate limiting").

# try:
#     response = LolWatcher.summoner.by_name(my_region, 'this_is_probably_not_anyones_summoner_name')
# except ApiError as err:
#     if err.response.status_code == 429:
#         print('We should retry in {} seconds.'.format(err.response.headers['Retry-After']))
#         print('this retry-after is handled by default by the RiotWatcher library')
#         print('future requests wait until the retry-after time passes')
#     elif err.response.status_code == 404:
#         print('Summoner with that ridiculous name not found.')
#     else:
#         raise