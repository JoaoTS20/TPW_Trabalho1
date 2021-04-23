from django.db import models
from django.contrib.auth.models import User


class NormalUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #Todo Adicionar aqui parâmetros como clubes_favoritos jogadores_favoritos e assim.
    #Talvez não parametros mas tabelas pra poderem ter mais do q um
    #Comentários que fez? tabela
    #Cargo Relacionado no Futebol (yes/no)? talvez


# podes adicionar mais fields no Player Team e Competition se quiseres
class Player(models.Model):
    POSITION_CHOICES = (
        ('ST', 'Striker'),
        ('LW', 'Left Winger'),
        ('RW', 'Right Winger'),
        ('CAM', 'Central Attacking Midfielder'),
        ('CM', 'Central Midfielder'),
        ('CDM', 'Central Defensive Midfielder'),
        ('LB', 'Left Back'),
        ('RB', 'Right Back'),
        ('CB', 'Center Back'),
        ('GR', 'Goalkeeper'),
    )
    BEST_FOOT = (('L', 'Left'), ('R', 'Right'))

    name = models.CharField(max_length=90)
    birthday = models.DateField()
    height = models.FloatField()
    nationality = models.CharField(max_length=70)
    position = models.CharField(max_length=3, choices=POSITION_CHOICES)
    best_foot = models.CharField(max_length=1, choices=BEST_FOOT)
    preferred_number = models.IntegerField()
    # player_img = models.CharField(max_length=100,default="default_player.png")
    # este pode-se adicionar depois
    # Talvez adicionar equipas passadas?
    # TODO: TROFÉUS CONQUISTADOS?


class Manager(models.Model):
    name = models.CharField(max_length=90)
    birthday = models.DateField()
    nationality = models.CharField(max_length=70)
    # TODO: RELACAO TAMBÉM PARA VER OS CLUBES QUE TREINOU?
    # TODO: TROFÉUS CONQUISTADOS?


class Team(models.Model):
    full_name = models.CharField(max_length=70)
    abreviated_name = models.CharField(max_length=4)
    founding_year = models.IntegerField()
    club_badge_img = models.CharField(max_length=100, default="default_club.png")
    # TODO: ALTEREI AQUI TALVEZ FAZER O MESMO COM COMPETITIONS E TEAMS
    players = models.ManyToManyField(Player, through='PlayerPlaysFor')
    city = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    # players = models.ManyToManyField(Player)
    # o players aqui pode ser mudado para o player talvez
    # TODO: TROFÉUS CONQUISTADOS?
    # TODO: CITY AND COUNTRY?
    # tem de se arranjar uma forma de adicionar talvez q uma competição acabou
    # para se apurar quem ganhou talvez?


class Competition(models.Model):
    full_name = models.CharField(max_length=70)
    competition_badge_img = models.CharField(max_length=100, default="default_league.png")
    #teams = models.ManyToManyField(Team)
    # pus as teams aqui porque assim podemos ter clubes a participarem em mais q uma competição
    # TODO: Pode ficar assim desde que não temos problemas com um clube sair da competição
    # TODO: A FAZER SEASON atributo aqui?

#Talvez pôr esta também
"""
class ManagerManages(models.Model):
    manager = models.ForeignKey(Manager,on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    season_joined = models.IntegerField()
    season_left = models.IntegerField(blank=True)
"""

# Se calhar fica melhor assim e podemos usar seasons
class ClubPlaysIn(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    competition = models.ForeignKey(Competition, on_delete=models.CASCADE)
    season = models.IntegerField()


# TODO: Criar a relação de Contrato (depois podiamos buscar clubes anteriores assim i sink)
class PlayerPlaysFor(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    # TODO: EM VEZ DE DATA COLOCAR SEASON?
    # sim se calhar fica melhor e interliga com os outros pk usam todos season
    date_joined = models.DateField()
    date_left = models.DateField(blank=True)


# TODO: EU pensar que aqui não falta nada. depois temos de ver como e se fazemos seasons
class Match(models.Model):
    ngame = models.IntegerField()
    home_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="home_team")
    away_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="away_team")
    competition = models.ForeignKey(Competition, on_delete=models.CASCADE)
    home_goals = models.IntegerField()
    away_goals = models.IntegerField()
    season = models.IntegerField()
    # Primeiro fazemos com isto e depois podemos adicionar marcadores e coisas assim
