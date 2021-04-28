from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
import datetime
from django.conf import settings as django_settings
import os

# Create your views here.
from django.urls import reverse

from app.forms import TeamFilterForm, SignUpForm, MakeCommentForm, FavouriteForm, \
    InsertCompetitionForm, InsertTeamForm, InsertPlayerForm, InsertStaffForm, InsertMatchForm, InsertClubPlaysInForm, \
    InsertStaffManagesForm, InsertPlayerPlaysForForm, InsertCompetitionsMatchesForm, PlayerFilterForm, \
    CompetitionFilterForm, StaffFilterForm
from app.models import Staff, Team, Competition, ClubPlaysIn, NormalUser, FavouriteTeam, Player, CommentCompetition, \
    Match, CommentPlayer, CommentMatch, PlayerPlaysFor, CompetitionsMatches, StaffManages, FavouritePlayer, CommentTeam, \
    FavouriteCompetition, CommentStaff


def test(request):
    t1 = Team(full_name="Futebol Clube do Porto",
              name="FC Porto",
              abreviated_name="FCP",
              country="Portugal",
              city="Porto",
              founding_year=1893,
              formation="4-4-2")
    t1.save()
    t2 = Team(full_name="Sport Lisboa e Benfica",
              abreviated_name="SLB",
              name="SL Benfica",
              formation="4-4-2",
              country="Portugal",
              city="Lisboa",
              founding_year=1904)
    t2.save()
    t3 = Team(full_name="Sporting Clube de Portugal",
              abreviated_name="SCP",
              name="SP Sporting",
              country="Portugal",
              city="Lisboa",
              formation="3-4-3",
              founding_year=1906)
    t3.save()
    t4 = Team(full_name="Sporting Clube de Braga",
              abreviated_name="SCB",
              name="SC Braga",
              formation="3-4-3",
              country="Portugal",
              city="Braga",
              founding_year=1921)
    t4.save()

    c = Competition(full_name="Liga NOS", region="Portugal")
    c.save()

    cpf = ClubPlaysIn(competition=c, team=t1, season="2020-2021")
    cpf.save()

    cpf = ClubPlaysIn(competition=c, team=t2, season="2020-2021")
    cpf.save()

    cpf = ClubPlaysIn(competition=c, team=t3, season="2020-2021")
    cpf.save()

    cpf = ClubPlaysIn(competition=c, team=t4, season="2020-2021")
    cpf.save()

    m1 = Match(ngame=1, competition=c, home_team=t1, away_team=t2,
               home_goals=3, away_goals=1, description="Matchday 1")
    m1.save()

    m2 = Match(ngame=1, competition=c, home_team=t3, away_team=t4,
               home_goals=2, away_goals=2, description="Matchday 1")
    m2.save()

    m3 = Match(ngame=2, competition=c, home_team=t3, away_team=t1,
               home_goals=1, away_goals=1, description="Matchday 2")
    m3.save()

    m4 = Match(ngame=2, competition=c, home_team=t2, away_team=t4,
               home_goals=4, away_goals=2, description="Matchday 2")
    m4.save()

    cm = CompetitionsMatches(competition=c, match=m1, season="2020-2021")
    cm.save()

    cm = CompetitionsMatches(competition=c, match=m2, season="2020-2021")
    cm.save()

    cm = CompetitionsMatches(competition=c, match=m3, season="2020-2021")
    cm.save()

    cm = CompetitionsMatches(competition=c, match=m4, season="2020-2021")
    cm.save()

    return render(request, 'test.html', {})


def home(request):
    return render(request, 'home.html', {})


def match_details(request, id):
    t_parms = {
        'match': Match.objects.get(id=id),
        'comments': CommentMatch.objects.get(match_id=id)
    }
    return render(request, 'match_details.html', t_parms)


# Competition Related:

def competitions(request):
    if request.method == 'POST':
        form = CompetitionFilterForm(request.POST)
        if form.is_valid():
            full_name = form.cleaned_data['full_name']
            region = form.cleaned_data['region']
            order = form.cleaned_data['order']
            print('Parameters:')
            print(full_name)
            print(order)
            if order != '':
                t_parms = {
                    'competitions': Competition.objects.filter(full_name__contains=full_name,
                                                               region__contains=region).order_by(order),
                    'form': CompetitionFilterForm()
                }
            else:
                t_parms = {
                    'competitions': Competition.objects.filter(full_name__contains=full_name, region__contains=region),
                    'form': CompetitionFilterForm()
                }
    else:
        t_parms = {
            'competitions': Competition.objects.all(),
            'form': CompetitionFilterForm()
        }
    return render(request, 'competitions.html', t_parms)


def competition_details(request, id, season='2020-2021'):
    teams = Team.objects.filter(clubplaysin__competition=id, clubplaysin__season=season)
    table = []
    for t in teams:
        dic = {
            "team": t, "points": 0, "home_goal": 0, "away_goal": 0,
            "home_concede": 0, "away_concede": 0,
            "win": 0, "draw": 0, "loss": 0
        }
        home_matches = Match.objects.filter(competitionsmatches__competition_id=id,
                                            competitionsmatches__season=season,
                                            home_team=t)
        for m in home_matches:
            if m.home_goals > m.away_goals:
                dic["win"] += 1
                dic["points"] += 3
            elif m.home_goals == m.away_goals:
                dic["draw"] += 1
                dic["points"] += 1
            else:
                dic["loss"] += 1
            dic["home_goal"] += m.home_goals
            dic["home_concede"] += m.away_goals
        away_matches = Match.objects.filter(competitionsmatches__competition_id=id,
                                            competitionsmatches__season=season,
                                            away_team=t)
        for m in away_matches:
            if m.home_goals < m.away_goals:
                dic["win"] += 1
                dic["points"] += 3
            elif m.home_goals == m.away_goals:
                dic["draw"] += 1
                dic["points"] += 1
            else:
                dic["loss"] += 1
            dic["away_goal"] += m.away_goals
            dic["away_concede"] += m.home_goals

        table.append(dic)
    table.sort(key=lambda k: -k["points"])
    print(table)
    if request.method == 'POST':
        if not request.user.is_authenticated or request.user.username == 'admin':
            return redirect('/login')
        normal = NormalUser.objects.get(user__username=request.user.username)
        print(normal.id)
        if 'remove' in request.POST:
            s = FavouriteCompetition.objects.get(competition_id=id, user_id=normal.id)
            s.delete()
            print("Removed from Favourites")
            return HttpResponseRedirect(str(id))
        elif 'add' in request.POST:
            s = FavouriteCompetition(competition_id=id, user_id=normal.id)
            s.save()
            print("Added to Favourites")
            return HttpResponseRedirect(str(id))
        form = MakeCommentForm(request.POST)
        if form.is_valid():
            comment = form.cleaned_data['comment']
            CommentCompetition(user=NormalUser.objects.get(user__username=request.user.username), comment=comment,
                               competition=Competition.objects.get(id=id)).save()
            return HttpResponseRedirect(str(id))

    if not request.user.is_authenticated or request.user.username == 'admin':
        favouritecompetition = False
    else:
        normal = NormalUser.objects.get(user__username=request.user.username)
        if FavouriteCompetition.objects.filter(competition_id=id, user_id=normal.id):
            favouritecompetition = True
            print("Está nos Favoritos")
        else:
            favouritecompetition = False
            print("Não está nos Favoritos")
    t_parms = {
        'competition': Competition.objects.get(id=id),
        'table': table,
        'teams': teams,
        'favouritecompetition': favouritecompetition,
        'formComment': MakeCommentForm(),
        'comments': CommentCompetition.objects.filter(competition_id=id),
        'matches': Match.objects.filter(competitionsmatches__competition_id=id, competitionsmatches__season=season),
        'seasons': ClubPlaysIn.objects.filter(competition_id=id).values_list('season', flat=True).distinct()
    }

    return render(request, 'competition_details.html', t_parms)


# Team Related


def teams(request):
    if request.method == 'POST':
        form = TeamFilterForm(request.POST)
        if form.is_valid():
            full_name = form.cleaned_data['full_name']
            country = form.cleaned_data['country']
            competition = form.cleaned_data['competition']
            order = form.cleaned_data['order']
            print('Parameters:')
            print(full_name)
            print(country)
            print(competition)
            print(order)
            if order != '':
                t_parms = {
                    'teams': Team.objects.filter(full_name__contains=full_name, country__contains=country,
                                                 clubplaysin__competition__full_name__contains=competition).order_by(
                        order),
                    'form': TeamFilterForm()
                }
            else:
                t_parms = {
                    'teams': Team.objects.filter(full_name__contains=full_name, country__contains=country,
                                                 clubplaysin__competition__full_name__contains=competition),
                    'form': TeamFilterForm()
                }
            # return render(request, 'teams.html', t_parms)
    else:
        t_parms = {
            'teams': Team.objects.all(),
            'form': TeamFilterForm()
        }
    return render(request, 'teams.html', t_parms)


def team_details(request, id, season='2020-2021'):
    if request.method == 'POST':
        if not request.user.is_authenticated or request.user.username == 'admin':
            return redirect('/login')
        normal = NormalUser.objects.get(user__username=request.user.username)
        print(normal.id)
        if 'remove' in request.POST:
            s = FavouriteTeam.objects.get(team_id=id, user_id=normal.id)
            s.delete()
            print("Removed from Favourites")
            return HttpResponseRedirect(str(id))
        elif 'add' in request.POST:
            s = FavouriteTeam(team_id=id, user_id=normal.id)
            s.save()
            print("Added to Favourites")
            return HttpResponseRedirect(str(id))
        form = MakeCommentForm(request.POST)
        if form.is_valid():
            comment = form.cleaned_data['comment']
            CommentTeam(user=NormalUser.objects.get(user__username=request.user.username), comment=comment,
                        team=Team.objects.get(id=id)).save()
            return HttpResponseRedirect(str(id))

    if not request.user.is_authenticated or request.user.username == 'admin':
        favouriteteam = False
    else:
        normal = NormalUser.objects.get(user__username=request.user.username)
        if FavouriteTeam.objects.filter(team_id=id, user_id=normal.id):
            favouriteteam = True
            print("Está nos Favoritos")
        else:
            favouriteteam = False
            print("Não está nos Favoritos")
    t_parms = {
        'team': Team.objects.get(id=id),
        'competitions': Competition.objects.filter(clubplaysin__team_id=id, clubplaysin__season=season),
        'players': Player.objects.filter(playerplaysfor__team_id=id, playerplaysfor__season=season),
        'seasons': ClubPlaysIn.objects.filter(team_id=id).values_list('season', flat=True).distinct(),
        'staff': StaffManages.objects.filter(team_id=id),
        'comments': CommentTeam.objects.filter(team_id=id),
        'favouriteteam': favouriteteam,
        'formComment': MakeCommentForm(),
    }
    return render(request, 'team_details.html', t_parms)


# Player Related

def players(request):
    if request.method == 'POST':
        form = PlayerFilterForm(request.POST)
        if form.is_valid():
            full_name = form.cleaned_data['full_name']
            position = form.cleaned_data['position']
            nationality = form.cleaned_data['nationality']
            foot = form.cleaned_data['foot']
            order = form.cleaned_data['order']
            print('Parameters:')
            print(full_name)
            print(position)
            print(nationality)
            print(foot)
            print(order)
            if order != '':
                t_parms = {
                    'players': Player.objects.filter(name__contains=full_name, position__contains=position,
                                                     nationality__contains=nationality,
                                                     best_foot__contains=foot).order_by(order),
                    'form': PlayerFilterForm()
                }
            else:
                t_parms = {
                    'players': Player.objects.filter(name__contains=full_name, position__contains=position,
                                                     nationality__contains=nationality, best_foot__contains=foot),
                    'form': PlayerFilterForm()
                }
            # return render(request, 'teams.html', t_parms)
    else:
        t_parms = {
            'players': Player.objects.all(),
            'form': PlayerFilterForm()
        }
    return render(request, 'players.html', t_parms)


def player_details(request, id):
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('/login')
        if request.user.username == 'admin':
            if 'delete' in request.POST:
                s = Player.objects.get(id=id)
                s.delete()
                print("Deleted")
                return redirect(reverse('players'))
            else:
                return redirect('/login')
        else:
            normal = NormalUser.objects.get(user__username=request.user.username)
            print(normal.id)
            if 'remove' in request.POST:
                s = FavouritePlayer.objects.get(player_id=id, user_id=normal.id)
                s.delete()
                print("Removed from Favourites")
                return HttpResponseRedirect(str(id))
            elif 'add' in request.POST:
                s = FavouritePlayer(player_id=id, user_id=normal.id)
                s.save()
                print("Added to Favourites")
                return HttpResponseRedirect(str(id))
            form = MakeCommentForm(request.POST)
            if form.is_valid():
                comment = form.cleaned_data['comment']
                CommentPlayer(user=NormalUser.objects.get(user__username=request.user.username), comment=comment,
                              player=Player.objects.get(id=id)).save()
                return HttpResponseRedirect(str(id))  # render(request, 'player_details.html', t_parms)

    if not request.user.is_authenticated:
        favouriteplayer = False
    else:
        if request.user.username == 'admin':
            deletebbt=True
            favouriteplayer = False
        else:
            normal = NormalUser.objects.get(user__username=request.user.username)
            if FavouritePlayer.objects.filter(player_id=id, user_id=normal.id):
                favouriteplayer = True
                print("Está nos Favoritos")
            else:
                favouriteplayer = False
                print("Não está nos Favoritos")
            deletebbt = False

    t_parms = {
        'player': Player.objects.get(id=id),
        'teams': set(Team.objects.filter(playerplaysfor__player_id=id).distinct()),  # TODO: Encontrar melhor solução
        'season': PlayerPlaysFor.objects.filter(player_id=id),
        'comments': CommentPlayer.objects.filter(player_id=id),
        'age': int((datetime.date.today() - Player.objects.get(id=id).birthday).days / 365),
        'favouriteplayer': favouriteplayer,
        'formComment': MakeCommentForm(),
        'deletebbt': deletebbt
    }
    return render(request, 'player_details.html', t_parms)


# Staff Related
def staff(request):
    if request.method == 'POST':
        form = StaffFilterForm(request.POST)
        if form.is_valid():
            full_name = form.cleaned_data['full_name']
            nationality = form.cleaned_data['nationality']
            function = form.cleaned_data['function']
            order = form.cleaned_data['order']
            print('Parameters:')
            print(full_name)
            print(nationality)
            print(function)
            print(order)
            if order != '':
                t_parms = {
                    'staffs': Staff.objects.filter(full_name__contains=full_name, function__contains=function, nationality__contains=nationality).order_by(
                        order),
                    'form': StaffFilterForm()
                }
            else:
                t_parms = {
                    'staffs': Staff.objects.filter(full_name__contains=full_name, function__contains=function, nationality__contains=nationality),
                    'form': StaffFilterForm()
                }
    else:
        t_parms = {
            'staffs': Staff.objects.all(),
            'form': StaffFilterForm()
        }
    return render(request, 'staff.html', t_parms)


def staff_details(request, id):
    if request.method == 'POST':
        if not request.user.is_authenticated or request.user.username == 'admin':
            return redirect('/login')
        normal = NormalUser.objects.get(user__username=request.user.username)
        print(normal.id)
        form = MakeCommentForm(request.POST)
        if form.is_valid():
            comment = form.cleaned_data['comment']
            CommentStaff(user=NormalUser.objects.get(user__username=request.user.username), comment=comment,
                         staff=Staff.objects.get(id=id)).save()
            return HttpResponseRedirect(str(id))  # render(request, 'player_details.html', t_parms)
    t_parms = {
        'staff': Staff.objects.get(id=id),
        'teams': Team.objects.filter(staffmanages__staff_id=id),
        'seasons': StaffManages.objects.filter(staff_id=id),
        'age': int((datetime.date.today() - Staff.objects.get(id=id).birthday).days / 365),
        'formComment': MakeCommentForm(),
    }
    return render(request, 'staff_details.html', t_parms)


# User Related

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            job_football_related = form.cleaned_data.get('job_football_related')
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            NormalUser(user=user, job_football_related=job_football_related).save()
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def profile(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    else:
        t_parms = {
            'userInfo': NormalUser.objects.get(user__username=request.user.username),
            'favouriteTeams': Team.objects.filter(favouriteteam__user__user_id=request.user.id),
            'favouritePlayers': Player.objects.filter(favouriteplayer__user__user_id=request.user.id),
            'favouriteCompetition': Competition.objects.filter(favouritecompetition__user__user_id=request.user.id)
        }
        return render(request, 'profile.html', t_parms)

"""
def insert_competition(request):
    # TODO: inserir autenticação
    if request.method == "POST":
        print("entrou aqui")
        print(request.FILES)
        form = InsertCompetitionForm(request.POST, request.FILES)
        if form.is_valid():

            c = Competition(full_name=form.cleaned_data["full_name"],
                            region=form.cleaned_data["region"])
            c.save()

            # Escrever ficheiro
            f = request.FILES['file']
            with open(os.path.join(django_settings.STATIC_ROOT,
                                   'img/competitions/' + str(c.id) + "." + f.name.split(".")[1]), 'wb+') as destination:
                for chunk in f.chunks():
                    destination.write(chunk)

            c.competition_badge_img = str(c.id) + "." + f.name.split(".")[1]
            c.save()
            return render(request, "insert_competition.html", {"form": form})
        else:
            print(form.errors)
    else:
        form = InsertCompetitionForm()
        return render(request, "insert_competition.html", {"form": form})
"""


# TODO: Meter os edit e os inserts que faltam !!!!!!!!!!!!!
def insert_team(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    if request.method == "POST":
        form = InsertTeamForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('teams'))#return render(request, "insert_all.html", {"form": form, "title": "Team"})
    form = InsertTeamForm()
    return render(request, "insert_all.html", {"form": form, "title": "Team"})


def insert_staff(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    if request.method == "POST":
        form = InsertStaffForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('staff'))#return render(request, "insert_all.html", {"form": form, "title": "Staff"})
    form = InsertStaffForm()
    return render(request, "insert_all.html", {"form": form, "title": "Staff"})


def insert_player(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    if request.method == "POST":
        form = InsertPlayerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('players')) #render(request, "insert_all.html", {"form": form, "title": "Player"})
    form = InsertPlayerForm()
    return render(request, "insert_all.html", {"form": form, "title": "Player"})


def insert_competition(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    if request.method == "POST":
        print(request.FILES)
        form = InsertCompetitionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('competitions'))#render(request, "insert_all.html", {"form": form, "title": "Competition"})
    form = InsertCompetitionForm()
    return render(request, "insert_all.html", {"form": form, "title": "Competition"})


def edit_team(request, id):
    if not request.user.is_authenticated:
        return redirect('/login')
    if request.method == "POST":
        form = InsertTeamForm(request.POST, request.FILES,instance=Team.objects.get(id=id))
        if form.is_valid():
            form.save()
            return redirect(reverse('team_details'),args=id)#return render(request, "edit_all.html", {"form": form, "title": "Team"})
        else:
            print(form.errors)
    form = InsertTeamForm(instance=Team.objects.get(id=id))
    return render(request, "edit_all.html", {"form": form, "title": "Team"})


def edit_staff(request, id):
    if not request.user.is_authenticated:
        return redirect('/login')
    if request.method == "POST":
        form = InsertStaffForm(request.POST, request.FILES,instance=Staff.objects.get(id=id))
        if form.is_valid():
            form.save()
            return redirect(reverse('staff_details'),args=id) #render(request, "edit_all.html", {"form": form, "title": "Staff"})
        else:
            print(form.errors)
    form = InsertStaffForm(instance=Staff.objects.get(id=id))
    return render(request, "edit_all.html", {"form": form, "title": "Staff"})


def edit_player(request, id):
    if not request.user.is_authenticated:
        return redirect('/login')
    if request.method == "POST":
        form = InsertPlayerForm(request.POST, request.FILES, instance=Player.objects.get(id=id))
        if form.is_valid():
            form.save()
            return redirect('player_details',str(id)) #render(request, "edit_all.html", {"form": form, "title": "Player"})
        else:
            print(form.errors)
    form = InsertPlayerForm(instance=Player.objects.get(id=id))
    return render(request, "edit_all.html", {"form": form, "title": "Player"})


def edit_competition(request, id):
    if not request.user.is_authenticated:
        return redirect('/login')
    if request.method == "POST":
        form = InsertCompetitionForm(request.POST, request.FILES, instance=Competition.objects.get(id=id))
        if form.is_valid():
            form.save()
            return redirect('competition_details',str(id)) #render(request, "edit_all.html", {"form": form, "title": "Competition"})
        else:
            print(form.errors)
    form = InsertCompetitionForm(instance=Competition.objects.get(id=id))
    return render(request, "edit_all.html", {"form": form, "title": "Competition"})


