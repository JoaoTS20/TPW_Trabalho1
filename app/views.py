from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
import datetime

# Create your views here.
from app.forms import TeamFilterForm, SignUpForm
from app.models import Staff, Team, Competition, ClubPlaysIn, NormalUser, FavouriteTeam, Player, CommentCompetition, \
    Match, CommentPlayer, CommentMatch, PlayerPlaysFor


def test(request):
    return render(request, 'test.html', {})


def home(request):
    return render(request, 'home.html', {})


def match_details(request, id):
    t_parms = {
        'match': Match.objects.get(id=id),
        'comments':CommentMatch.objects.get(match_id=id)
    }
    return render(request, 'match_details.html', t_parms)


# Competition Related:

def competitions(request):
    t_parms = {
        'competitions': Competition.objects.all()
    }
    return render(request, 'competitions.html', t_parms)


def competition_details(request, id, season='2020-2021'):
    t_parms = {
        'competition': Competition.objects.get(id=id),
        'teams': Team.objects.filter(clubplaysin__competition_id=id, clubplaysin__season=season),
        'comments': CommentCompetition.objects.filter(competition_id=id),
        'matches': Match.objects.filter(competitionsmatches__competition_id=id, competitionsmatches__season=season)
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

            t_parms = {
                'teams': Team.objects.filter(full_name__contains=full_name, country__contains=country,
                                             clubplaysin__competition__full_name__contains=competition),
                'form': TeamFilterForm()
            }
            return render(request, 'teams.html', t_parms)
    else:
        t_parms = {
            'teams': Team.objects.all(),
            'form': TeamFilterForm()
        }
    return render(request, 'teams.html', t_parms)


def team_details(request, id, season='2020-2021'):
    t_parms = {
        'team': Team.objects.get(id=id),
        'competitions': Competition.objects.filter(clubplaysin__team_id=id, clubplaysin__season=season),
        'players': Player.objects.filter(playerplaysfor__team_id=id, playerplaysfor__season=season)
    }
    return render(request, 'team_details.html', t_parms)


# Player Related

def players(request):
    return render(request, 'players.html', {'players': Player.objects.all()})


def player_details(request, id):
    t_parms = {
        'player': Player.objects.get(id=id),
        'teams': Team.objects.filter(playerplaysfor__player_id=id),
        'season':PlayerPlaysFor.objects.filter(player_id=id),
        'comments': CommentPlayer.objects.filter(player_id=id)
    }
    return render(request, 'player_details.html', t_parms)

# Staff Related
def staff(request):
        t_parms={
            'staffs': Staff.objects.all(),
        }
        return render(request,'staff.html', t_parms)

def staff_details(request,id):
        t_parms={
            'staff': Staff.objects.get(id=id),
            'teams': Team.objects.filter(managermanages__staff_id=id)
        }
        return render(request,'staff_details.html', t_parms)
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
