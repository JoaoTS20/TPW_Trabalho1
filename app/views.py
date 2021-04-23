from django.shortcuts import render


# Create your views here.

def test(request):
    return render(request, 'test.html', {})


def home(request):
    return render(request, 'home.html', {})


def competitions(request):
    return render(request, 'competitions.html', {})


def teams(request):
    return render(request, 'teams.html', {})

def players(request):
    return render(request, 'players.html', {})
