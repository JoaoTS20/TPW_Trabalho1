from django.db import models
from django.contrib.auth.models import User

from django.core.validators import RegexValidator

# Todo Hugo Comments Players,Games,Competitions
# Adicionar str aos models e adicionar name no team

class Player(models.Model):
    POSITION_CHOICES = ( #Isto está trocado!!!!!!!!! meter cena de full name
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
    BEST_FOOT = (('L', 'Left'), ('R', 'Right')) #Isto está trocado!!!!!!!!!

    name = models.CharField(max_length=90)
    birthday = models.DateField()
    height = models.FloatField()
    nationality = models.CharField(max_length=70)
    position = models.CharField(max_length=3, choices=POSITION_CHOICES)
    best_foot = models.CharField(max_length=1, choices=BEST_FOOT)
    preferred_number = models.IntegerField()
    player_img = models.CharField(max_length=100, default="default_player.png")
    # TODO: TROFÉUS CONQUISTADOS?

    def to_dict(self):
        return {
            "name": self.name, "birthday": self.birthday, "height": self.height,
            "nationality": self.nationality, "position": self.position,
            "best_foot": self.best_foot, "preferred_number": self.preferred_number,
            "player_img": self.player_img
        }


class Staff(models.Model): #ACRESCENTAR IMAGE
    name = models.CharField(max_length=90)
    birthday = models.DateField()
    nationality = models.CharField(max_length=70)
    function = models.CharField(max_length=70)
    # TODO: TROFÉUS CONQUISTADOS?


class Team(models.Model):
    full_name = models.CharField(max_length=70)
    #name= models.CharField(max_length=70)
    abreviated_name = models.CharField(max_length=4)
    founding_year = models.IntegerField()
    club_badge_img = models.CharField(max_length=100, default="default_club.png")
    city = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    players = models.ManyToManyField(Player, through='PlayerPlaysFor')

    # TODO: TROFÉUS CONQUISTADOS?

    # tem de se arranjar uma forma de adicionar talvez q uma competição acabou
    # para se apurar quem ganhou talvez?

    def to_dict(self):
        return {
            "full_name": self.full_name, "abreviated_name": self.abreviated_name,
            "founding_year": self.founding_year, "club_badge_img": self.club_badge_img,
            "city": self.city, "country": self.country
        }


# Adicionei o tipo de competição
class Competition(models.Model):
    full_name = models.CharField(max_length=70)
    competition_badge_img = models.CharField(max_length=100, default="default_league.png")
    teams = models.ManyToManyField(Team, through='ClubPlaysIn')
    """season = models.CharField(max_length=5, validators=[RegexValidator(
        regex='[0-9]{4}-[0-9]{4}',
        message='Season must follow the format year-year',
        code='invalid_season'
    )])"""

    def to_dict(self):
        return {
            "full_name": self.full_name, "competition_badge_img": self.competition_badge_img
        }


# Primeiro fazemos com isto e depois podemos adicionar marcadores e coisas assim
class Match(models.Model):
    ngame = models.CharField(max_length=50)  # Todo Hugo Talvez mudar isto para descrição jogo ou assim para ser 'MatchDay 38' ou 'SEMI-FINALS'
    # Talvez seja uma boa ideia mas não sei como podemos ordenar depois ?
    # Talvez possamos criar outro atributo com descrição e assim usando o ngame pra ordenar
    description = models.CharField(max_length=25)
    home_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="home_team")
    away_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="away_team")
    competition = models.ForeignKey(Competition, on_delete=models.CASCADE)
    home_goals = models.IntegerField()
    away_goals = models.IntegerField()
    """season = models.CharField(max_length=9, validators=[RegexValidator(
        regex='[0-9]{4}-[0-9]{4}',
        message='Season must follow the format year-year',
        code='invalid_season'
    )])"""

    def to_dict(self):
        return {
            "ngame": self.ngame, "description": self.description,
            "home_team": self.home_team.to_dict(), "away_team": self.away_team.to_dict(),
            "competition": self.competition.to_dict(), "home_goals": self.home_goals,
            "away_goals": self.away_goals
        }


# Equipa joga em determinada Competicão (de terminada época) (Penso que podemos alterar para o manytomanyfield e não preciso isto)
class ClubPlaysIn(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    competition = models.ForeignKey(Competition, on_delete=models.CASCADE)
    season = models.CharField(max_length=9, validators=[RegexValidator(
        regex='[0-9]{4}-[0-9]{4}',
        message='Season must follow the format year-year',
        code='invalid_season'
    )])


# Treinador da Equipa em Determinada Época (Também dá para buscar clubes do treinador em cada época)
class ManagerManages(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    season = models.CharField(max_length=9, validators=[RegexValidator(
        regex='[0-9]{4}-[0-9]{4}',
        message='Season must follow the format year-year',
        code='invalid_season'
    )])


# Jogadores da Equipa em Determinada Época (Também dá para buscar clubes do jogador em cada época)
class PlayerPlaysFor(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    season = models.CharField(max_length=9, validators=[RegexValidator(
        regex='[0-9]{4}-[0-9]{4}',
        message='Season must follow the format year-year',
        code='invalid_season'
    )])


class CompetitionsMatches(models.Model):
    competition = models.ForeignKey(Competition, on_delete=models.CASCADE)
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    season = models.CharField(max_length=9, validators=[RegexValidator(
        regex='[0-9]{4}-[0-9]{4}',
        message='Season must follow the format year-year',
        code='invalid_season'
    )])


class NormalUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    job_football_related = models.BooleanField()
    favouriteplayers = models.ManyToManyField(Player, through='FavouritePlayer')
    favouriteteams = models.ManyToManyField(Team, through='FavouriteTeam')
    favouritecompetitions = models.ManyToManyField(Competition, through='FavouriteCompetition')
    # Todo Hugo Tabelas Clubes_Favoritos Jogadores_Favoritos Competição Favorita! ou manytomanyfield simples


# Não sei se será preciso mais algum atributo?

class FavouritePlayer(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    user = models.ForeignKey(NormalUser, on_delete=models.CASCADE)


class FavouriteTeam(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    user = models.ForeignKey(NormalUser, on_delete=models.CASCADE)


class FavouriteCompetition(models.Model):
    competition = models.ForeignKey(Competition, on_delete=models.CASCADE)
    user = models.ForeignKey(NormalUser, on_delete=models.CASCADE)


class CommentPlayer(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    user = models.ForeignKey(NormalUser, on_delete=models.CASCADE)
    timeofpost = models.DateTimeField()
    comment = models.CharField(max_length=120)


class CommentMatch(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    user = models.ForeignKey(NormalUser, on_delete=models.CASCADE)
    timeofpost = models.DateTimeField()
    comment = models.CharField(max_length=120)


class CommentCompetition(models.Model):
    competition = models.ForeignKey(Competition, on_delete=models.CASCADE)
    user = models.ForeignKey(NormalUser, on_delete=models.CASCADE)
    timeofpost = models.DateTimeField()
    comment = models.CharField(max_length=120)
