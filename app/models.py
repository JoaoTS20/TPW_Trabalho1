from datetime import datetime

from django.db import models
from django.contrib.auth.models import User

from django.core.validators import RegexValidator


class Player(models.Model):
    POSITION_CHOICES = (
        ('Striker', 'ST-Striker'),
        ('Left Winger', 'LW-Left Winger'),
        ('Right Winger', 'RW-Right Winger'),
        ('Central Attacking Midfielder', 'CAM-Central Attacking Midfielder'),
        ('Central Midfielder', 'CM-Central Midfielder'),
        ('Central Defensive Midfielder', 'CDM-Central Defensive Midfielder'),
        ('Left Back', 'LB-Left Back'),
        ('Right Back', 'RB-Right Back'),
        ('Center Back', 'CB-Center Back'),
        ('Goalkeeper', 'GR-Goalkeeper'),
    )
    BEST_FOOT = (('Left', 'L-Left'), ('Right', 'R-Right'), ('Both', 'B-Both'))

    full_name = models.CharField(max_length=120)
    name = models.CharField(max_length=90)
    birthday = models.DateField()
    height = models.FloatField()
    nationality = models.CharField(max_length=70)
    position = models.CharField(max_length=28, choices=POSITION_CHOICES)
    best_foot = models.CharField(max_length=5, choices=BEST_FOOT)
    preferred_number = models.IntegerField()
    player_img = models.CharField(max_length=100, default="default_player.png")

    def to_dict(self):
        return {
            "name": self.name, "birthday": self.birthday, "height": self.height,
            "nationality": self.nationality, "position": self.position,
            "best_foot": self.best_foot, "preferred_number": self.preferred_number,
            "player_img": self.player_img
        }

    def __str__(self):
        return self.full_name + '-' + self.name


class Staff(models.Model):
    full_name = models.CharField(max_length=120)
    name = models.CharField(max_length=90)
    birthday = models.DateField()
    nationality = models.CharField(max_length=70)
    function = models.CharField(max_length=70)
    staff_img = models.CharField(max_length=100, default="default_staff.png")

    def __str__(self):
        return self.full_name


class Team(models.Model):
    full_name = models.CharField(max_length=70)
    name = models.CharField(max_length=70)
    abreviated_name = models.CharField(max_length=4)
    founding_year = models.IntegerField()
    club_badge_img = models.CharField(max_length=100, default="default_club.png")
    city = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    players = models.ManyToManyField(Player, through='PlayerPlaysFor')
    formation = models.CharField(max_length=5, validators=[RegexValidator(
        regex='[0-9]{1}-[0-9]{1}-[0-9]{1}',
        message='Season must follow the format number-number-number',
        code='invalid_formation'
    )])

    def to_dict(self):
        return {
            "full_name": self.full_name, "abreviated_name": self.abreviated_name,
            "founding_year": self.founding_year, "club_badge_img": self.club_badge_img,
            "city": self.city, "country": self.country
        }

    def __str__(self):
        return self.full_name


class Competition(models.Model):
    full_name = models.CharField(max_length=70)
    competition_badge_img = models.CharField(max_length=100, default="default_league.png")
    teams = models.ManyToManyField(Team, through='ClubPlaysIn')
    region = models.CharField(max_length=70)
    """season = models.CharField(max_length=5, validators=[RegexValidator(
        regex='[0-9]{4}-[0-9]{4}',
        message='Season must follow the format year-year',
        code='invalid_season'
    )])"""

    def to_dict(self):
        return {
            "full_name": self.full_name, "competition_badge_img": self.competition_badge_img
        }

    def __str__(self):
        return self.full_name


# Primeiro fazemos com isto e depois podemos adicionar marcadores e coisas assim
class Match(models.Model):
    ngame = models.IntegerField()
    description = models.CharField(max_length=25) # Descrição 'MatchDay 38' ou 'SEMI-FINALS'
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

    def __str__(self):
        return self.description


# Equipa joga em determinada Competicão (de terminada época)
class ClubPlaysIn(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    competition = models.ForeignKey(Competition, on_delete=models.CASCADE)
    season = models.CharField(max_length=9, validators=[RegexValidator(
        regex='[0-9]{4}-[0-9]{4}',
        message='Season must follow the format year-year',
        code='invalid_season'
    )])

    def __str__(self):
        return self.team.full_name + '-' + self.competition.full_name + '-' + self.season


# Treinador da Equipa em Determinada Época (Também dá para buscar clubes do treinador em cada época)
class StaffManages(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    season = models.CharField(max_length=9, validators=[RegexValidator(
        regex='[0-9]{4}-[0-9]{4}',
        message='Season must follow the format year-year',
        code='invalid_season'
    )])

    def __str__(self):
        return self.staff.full_name + '-' + self.team.full_name + '-' + self.season


# Jogadores da Equipa em Determinada Época (Também dá para buscar clubes do jogador em cada época)
class PlayerPlaysFor(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    season = models.CharField(max_length=9, validators=[RegexValidator(
        regex='[0-9]{4}-[0-9]{4}',
        message='Season must follow the format year-year',
        code='invalid_season'
    )])

    def __str__(self):
        return self.player.full_name + '-' + self.team.full_name + '-' + self.season


class CompetitionsMatches(models.Model):
    competition = models.ForeignKey(Competition, on_delete=models.CASCADE)
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    season = models.CharField(max_length=9, validators=[RegexValidator(
        regex='[0-9]{4}-[0-9]{4}',
        message='Season must follow the format year-year',
        code='invalid_season'
    )])

    def __str__(self):
        return self.competition.full_name + '-' + self.match + '-' + self.season


class NormalUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    job_football_related = models.BooleanField()
    favouriteplayers = models.ManyToManyField(Player, through='FavouritePlayer')
    favouriteteams = models.ManyToManyField(Team, through='FavouriteTeam')
    favouritecompetitions = models.ManyToManyField(Competition, through='FavouriteCompetition')

    def __str__(self):
        return self.user.username


class FavouritePlayer(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    user = models.ForeignKey(NormalUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.player.full_name + '-' + self.user.user.username


class FavouriteTeam(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    user = models.ForeignKey(NormalUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.team.full_name + '-' + self.user.user.username


class FavouriteCompetition(models.Model):
    competition = models.ForeignKey(Competition, on_delete=models.CASCADE)
    user = models.ForeignKey(NormalUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.competition.full_name + '-' + self.user


# Comments

class CommentPlayer(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    user = models.ForeignKey(NormalUser, on_delete=models.CASCADE)
    timeofpost = models.DateTimeField(default=datetime.now)
    comment = models.CharField(max_length=120)

    def __str__(self):
        return self.player.full_name + '-' + self.user.user.username + '-' + self.comment


class CommentMatch(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    user = models.ForeignKey(NormalUser, on_delete=models.CASCADE)
    timeofpost = models.DateTimeField(default=datetime.now)
    comment = models.CharField(max_length=120)

    def __str__(self):
        return self.match.description + '-' + self.user.user.username + '-' + self.comment


class CommentCompetition(models.Model):
    competition = models.ForeignKey(Competition, on_delete=models.CASCADE)
    user = models.ForeignKey(NormalUser, on_delete=models.CASCADE)
    timeofpost = models.DateTimeField(default=datetime.now)
    comment = models.CharField(max_length=120)

    def __str__(self):
        return self.competition.full_name + '-' + self.user.user.username + '-' + self.comment


class CommentTeam(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    user = models.ForeignKey(NormalUser, on_delete=models.CASCADE)
    timeofpost = models.DateTimeField(default=datetime.now)
    comment = models.CharField(max_length=120)

    def __str__(self):
        return self.team.full_name + '-' + self.user.user.username + '-' + self.comment
