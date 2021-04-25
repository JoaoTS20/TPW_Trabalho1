from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
import datetime

# Create your views here.
from app.forms import TeamFilterForm, SignUpForm
from app.models import Staff, Team, Competition, ClubPlaysIn, NormalUser


def test(request):
    return render(request, 'test.html', {})


def home(request):
    return render(request, 'home.html', {})


def competitions(request):
    return render(request, 'competitions.html', {})


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


def team_details(request, id):
    t_parms = {
        'team': Team.objects.get(id=id)
    }
    return render(request, 'team_details.html', t_parms)


def players(request):
    return render(request, 'players.html', {})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            job_football_related = form.cleaned_data.get('job_football_related')
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            NormalUser(user=user,job_football_related=job_football_related).save()
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def profile(request):
    return render(request, 'profile.html', {})
