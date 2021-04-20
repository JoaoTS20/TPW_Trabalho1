from django.db import models

#podes adicionar mais fields no Player Team e Competition se quiseres
class Player(models.Model):
    name = models.CharField(max_length=70)
    birthday = models.DateField()
    #player_img = models.CharField(max_length=100,default="default_player.png")
    #este pode-se adicionar depois

class Team(models.Model):
    full_name = models.CharField(max_length=70)
    abreviated_name = models.CharField(max_length=4)
    founding_year = models.IntegerField()
    club_badge_img = models.CharField(max_length=100,default="default_club.png")
    players = models.ManyToManyField(Player)
    #o players aqui pode ser mudado para o player talvez


class Competition(models.Model):
    full_name = models.CharField(max_length=70)
    competition_badge_img = models.CharField(max_length=100,default="default_league.png")
    teams = models.ManyToManyField(Team)
    #pus as teams aqui porque assim podemos ter clubes a participarem em mais q uma competição



class Match(models.Model):
    ngame = models.IntegerField()
    home_team = models.ForeignKey(Team,on_delete=models.CASCADE, related_name="home_team")
    away_team = models.ForeignKey(Team,on_delete=models.CASCADE, related_name="away_team")
    competition = models.ForeignKey(Competition,on_delete=models.CASCADE)
    home_goals = models.IntegerField()
    away_goals = models.IntegerField()
    season = models.IntegerField()
    # Primeiro fazemos com isto e depois podemos adicionar marcadores e coisas assim
