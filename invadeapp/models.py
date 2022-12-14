from django.db import models

class Champions(models.Model):
    key = models.IntegerField() 
    name = models.CharField(max_length=200)
    attack = models.IntegerField() 
    defense = models.IntegerField() 
    magic = models.IntegerField() 
    difficulty = models.IntegerField() 
    hp = models.FloatField()
    hpperlevel = models.FloatField()
    mp = models.FloatField()
    mpperlevel = models.FloatField()
    movespeed = models.FloatField()
    armor = models.FloatField()
    armorperlevel = models.FloatField()
    spellblock = models.FloatField()
    spellblockperlevel = models.FloatField()
    attackrange = models.FloatField()
    hpregen = models.FloatField()
    hpregenperlevel = models.FloatField()
    mpregen = models.FloatField()
    mpregenperlevel = models.FloatField()
    crit = models.FloatField()
    critperlevel = models.FloatField()
    attackdamage = models.FloatField()
    attackdamageperlevel = models.FloatField()
    attackspeedperlevel = models.FloatField()
    attackspeed = models.FloatField()
    image = models.CharField(max_length=100, default='meh')

    def __str__(self):
        return self.name

class PlayerRecord(models.Model):
    summoner_name = models.CharField(max_length=100)
    eid = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.summoner_name

class MatchData(models.Model):
    summoner_name_match = models.CharField(max_length=100, null=True, blank=True)
    team_id = models.CharField(max_length=10, null=True, blank=True)
    champion_id = models.CharField(max_length=100, null=True, blank=True)
    spell1_id = models.CharField(max_length=4, null=True, blank=True)
    spell2_id  = models.CharField(max_length=4, null=True, blank=True)

    def __str__(self):
        return self.summoner_name_match



