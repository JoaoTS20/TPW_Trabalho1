from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
import datetime
from django.conf import settings as django_settings
import os

# Create your views here.
from django.urls import reverse

from app.forms import TeamFilterForm, SignUpForm, MakeCommentForm, FavouriteForm, \
    InsertCompetitionForm, InsertTeamForm, InsertPlayerForm, InsertStaffForm, InsertMatchForm, InsertClubPlaysInForm, \
    InsertStaffManagesForm, InsertPlayerPlaysForForm, PlayerFilterForm, \
    CompetitionFilterForm, StaffFilterForm
from app.models import Staff, Team, Competition, ClubPlaysIn, NormalUser, FavouriteTeam, Player, CommentCompetition, \
    Match, CommentPlayer, CommentMatch, PlayerPlaysFor, CompetitionsMatches, StaffManages, FavouritePlayer, CommentTeam, \
    FavouriteCompetition, CommentStaff


def error_render(request, code, desc):
    return render(request, "error.html", {"code": code, "desc": desc})


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

    t5 = Team(full_name="Futebol Clube Paços de Ferreira",
              abreviated_name="FCPF",
              name="Paços de Ferreira",
              formation="4-3-3",
              country="Portugal",
              city="Paços de Ferreira",
              founding_year=1950)
    t5.save()

    t6 = Team(full_name="Vitória Sport Clube",
              abreviated_name="VSC",
              name="Vitória de Guimarães",
              formation="4-3-3",
              country="Portugal",
              city="Guimarães",
              founding_year=1922)
    t6.save()
    t7 = Team(full_name="Moreirense Futebol Clube",
              abreviated_name="MFC",
              name="Moreirense",
              formation="3-4-3",
              country="Portugal",
              city="Moreira de Cónegos",
              founding_year=1938)
    t7.save()
    t8 = Team(full_name="Clube Desportivo Santa Clara",
              abreviated_name="CDSC",
              name="Santa Clara",
              formation="4-3-3",
              country="Portugal",
              city="Ponta Delgada",
              founding_year=1927)
    t8.save()
    t9 = Team(full_name="Clube Desportivo de Tondela",
              abreviated_name="CDT",
              name="Tondela",
              formation="4-3-3",
              country="Portugal",
              city="Tondela",
              founding_year=1933)
    t9.save()
    t10 = Team(full_name="Os Belenenses Futebol, SAD",
               abreviated_name="BEL",
               name="Belenenses SAD",
               formation="3-4-3",
               country="Portugal",
               city="Lisboa",
               founding_year=2018)
    t10.save()
    t11 = Team(full_name="Futebol Clube de Famalicão",
               abreviated_name="FCF",
               name="FC Famalicão",
               formation="4-3-3",
               country="Portugal",
               city="Vila Nova de Familicão",
               founding_year=1931)
    t11.save()
    t12 = Team(full_name="Portimonense Sporting Clube",
               abreviated_name="PSC",
               name="Portimonense",
               formation="4-3-3",
               country="Portugal",
               city="Portimão",
               founding_year=1914)
    t12.save()
    t13 = Team(full_name="Gil Vicente Futebol Clube",
               abreviated_name="GVFC",
               name="Gil Vicente",
               formation="4-3-3",
               country="Portugal",
               city="Barcelos",
               founding_year=1924)
    t13.save()
    t14 = Team(full_name="Club Sport Marítimo",
               abreviated_name="CSM",
               name="Marítimo",
               formation="4-5-1",
               country="Portugal",
               city="Funchal",
               founding_year=1910)
    t14.save()
    t15 = Team(full_name="Clube Desportivo Nacional",
               abreviated_name="CDN",
               name="Nacional",
               formation="3-5-2",
               country="Portugal",
               city="Funchal",
               founding_year=1910)
    t15.save()

    t16 = Team(full_name="Rio Ave Futebol Clube",
               abreviated_name="Rio",
               name="Rio Ave",
               formation="4-3-3",
               country="Portugal",
               city="Vila do Conde",
               founding_year=1939)
    t16.save()

    t17 = Team(full_name="Boavista Futebol Clube",
               abreviated_name="Boa",
               name="Boavista FC",
               formation="3-4-3",
               country="Portugal",
               city="Porto",
               founding_year=1903)
    t17.save()

    t18 = Team(full_name="Sporting Clube Farense",
               abreviated_name="SCF",
               name="SC Farense",
               formation="4-5-1",
               country="Portugal",
               city="Faro",
               founding_year=1910)
    t18.save()

    p1 = Player(full_name="Diogo António Cupido Gonçalves", name="Diogo Gonçalves", height=1.78,
                nationality="Portuguese", position="Right Back", best_foot="Right", preferred_number=17,
                birthday="1997-02-06")
    p1.save()

    p2 = Player(full_name="Jan Bert Lieve Vertonghen", name="Jan Vertonghen", height=1.89, nationality="Belgium",
                position="Center Back", best_foot="Left", preferred_number=5, birthday="1987-04-24")
    p2.save()

    p3 = Player(full_name="Nicolás Hernán Gonzalo Otamendi", name="Otamendi", height=1.83, nationality="Argentine",
                position="Center Back", best_foot="Right", preferred_number=30, birthday="1988-02-12")
    p3.save()

    p4 = Player(full_name="André Gomes Magalhães de Almeida",
                name="André Almeida",
                height=1.86,
                nationality="Portuguese",
                position="Right Back",
                best_foot="Right",
                preferred_number=34,
                birthday="1990-09-10")
    p4.save()

    p5 = Player(full_name="Francisco Leonel Lima Silva Machado",
                name="Chiquinho",
                height=1.74,
                nationality="Portuguese",
                position="Central Attacking Midfielder",
                best_foot="Right",
                preferred_number=10,
                birthday="1995-07-19")
    p5.save()
    p6 = Player(full_name="Julian Weigl",
                name="Julian Weigl",
                height=1.86,
                nationality="German",
                position="Central Defensive Midfielder",
                best_foot="Right",
                preferred_number=6,
                birthday="1995-09-08")
    p6.save()
    p7 = Player(full_name="Luís Miguel Afonso Fernandes",
                name="Pizzi",
                height=1.76,
                nationality="Portuguese",
                position="Central Attacking Midfielder",
                best_foot="Right",
                preferred_number=21,
                birthday="1989-10-06")
    p7.save()
    p8 = Player(full_name="Rafael Alexandre Fernandes Ferreira Silva",
                name="Rafa",
                height=1.70,
                nationality="Portuguese",
                position="Right Winger",
                best_foot="Right",
                preferred_number=7,
                birthday="1993-05-17")
    p8.save()
    p9 = Player(full_name="Képler Laveran Lima Ferreira",
                name="Pepe",
                height=1.88,
                nationality="Portuguese",
                position="Center Back",
                best_foot="Right",
                preferred_number=3,
                birthday="1983-02-26")
    p9.save()
    p10 = Player(full_name="Agustin Federico Marchesin",
                 name="Marchesin",
                 height=1.88,
                 nationality="Argentine",
                 position="Goalkeeper",
                 best_foot="Right",
                 preferred_number=1,
                 birthday="1988-03-16")
    p10.save()
    p11 = Player(full_name="Francisco Fernandes da Conceição",
                 name="Francisco Conceição",
                 height=1.70,
                 nationality="Portuguese",
                 position="Right Winger",
                 best_foot="Left",
                 preferred_number=10,
                 birthday="2002-12-14")
    p11.save()
    p12 = Player(full_name="Rui Filipe Caetano Moura",
                 name="Carraça",
                 height=1.77,
                 nationality="Portuguese",
                 position="Right Back",
                 best_foot="Right",
                 preferred_number=2,
                 birthday="1993-03-01")
    p12.save()
    p13 = Player(full_name="Diogo Filipe Monteiro Pinto Leite",
                 name="Diogo Leite",
                 height=1.88,
                 nationality="Portuguese",
                 position="Center Back",
                 best_foot="Left",
                 preferred_number=4,
                 birthday="1999-01-23")
    p13.save()
    p14 = Player(full_name="Fábio Daniel Ferreira Vieira",
                 name="Fábio Vieira",
                 height=1.70,
                 nationality="Portuguese",
                 position="Central Attacking Midfielder",
                 best_foot="Left",
                 preferred_number=10,
                 birthday="2000-05-30")
    p14.save()
    p15 = Player(full_name="Jesús Manuel Corona Ruíz",
                 name="Jesús Corona",
                 height=1.73,
                 nationality="Mexican",
                 position="Right Winger",
                 best_foot="Right",
                 preferred_number=17,
                 birthday="1993-01-06")
    p15.save()
    p16 = Player(full_name="Sérgio Miguel Relvas de Oliveira",
                 name="Sérgio Oliveira",
                 height=1.81,
                 nationality="Portuguese",
                 position="Central Midfielder",
                 best_foot="Right",
                 preferred_number=8,
                 birthday="1992-06-02")
    p16.save()
    p17 = Player(full_name="Jovane Eduardo Borges Cabral",
                 name="Jovane Cabral",
                 height=1.76,
                 nationality="Cape Verdean",
                 position="Left Winger",
                 best_foot="Right",
                 preferred_number=7,
                 birthday="1998-06-14")
    p17.save()
    p18 = Player(full_name="Nuno Alexandre Tavares Mendes",
                 name="Nuno Mendes",
                 height=1.76,
                 nationality="Portuguese",
                 position="Left Back",
                 best_foot="Left",
                 preferred_number=5,
                 birthday="2002-06-19")
    p18.save()

    p19 = Player(full_name="Luís Carlos Novo Neto",
                 name="Luís Neto",
                 height=1.87,
                 nationality="Portuguese",
                 position="Center Back",
                 best_foot="Right",
                 preferred_number=3,
                 birthday="1988-05-26")
    p19.save()

    p20 = Player(full_name="",
                 name="João Palhinha",
                 height=1.90,
                 nationality="Portuguese",
                 position="Central Defensive Midfielder",
                 best_foot="Right",
                 preferred_number=6,
                 birthday="1995-07-09")
    p20.save()
    p21 = Player(full_name="João Mário Naval da Costa Eduardo",
                 name="João Mário",
                 height=1.79,
                 nationality="Portuguese",
                 position="Central Midfielder",
                 best_foot="Right",
                 preferred_number=10,
                 birthday="1993-01-19")
    p21.save()
    p22 = Player(full_name="Daniel Santos Bragança",
                 name="Daniel Bragança",
                 height=1.76,
                 nationality="Portuguese",
                 position="Central Defensive Midfielder",
                 best_foot="Right",
                 preferred_number=6,
                 birthday="1999-05-27")
    p22.save()
    p23 = Player(full_name="Nuno Miguel Gomes dos Santos",
                 name="Nuno Santos",
                 height=1.76,
                 nationality="Portuguese",
                 position="Left Winger",
                 best_foot="Left",
                 preferred_number=11,
                 birthday="1995-02-13")
    p23.save()
    p24 = Player(full_name="Pedro António Pereira Gonçalves",
                 name="Pedro Gonçalves",
                 height=1.73,
                 nationality="Portuguese",
                 position="Central Attacking Midfielder",
                 best_foot="Right",
                 preferred_number=8,
                 birthday="1998-06-28")
    p24.save()

    p25 = Player(full_name="Nuno Miguel Ribeiro Cruz Jerónimo Sequeira",
                 name="Nuno Sequeira",
                 height=1.84,
                 nationality="Portuguese",
                 position="Left Back",
                 best_foot="Left",
                 preferred_number=5,
                 birthday="1990-08-19")
    p25.save()

    p26 = Player(full_name="David Mota Veiga Teixeira Carmo",
                 name="David Carmo",
                 height=1.96,
                 nationality="Portuguese",
                 position="Center Back",
                 best_foot="Right",
                 preferred_number=2,
                 birthday="1999-07-19")
    p26.save()

    p27 = Player(full_name="Osvaldo Fabián Nicolás Gaitán",
                 name="Nico Gaitán",
                 height=1.74,
                 nationality="Argentine",
                 position="Left Winger",
                 best_foot="Right",
                 preferred_number=10,
                 birthday="1988-02-23")
    p27.save()

    p28 = Player(full_name="Ricardo Sousa Esgaio",
                 name="Ricardo Esgaio",
                 height=1.73,
                 nationality="Portuguese",
                 position="Right Back",
                 best_foot="Right",
                 preferred_number=2,
                 birthday="1993-05-16")
    p28.save()

    p29 = Player(full_name="João Pedro Barradas Novais",
                 name="João Novais",
                 height=1.80,
                 nationality="Portuguese",
                 position="Central Attacking Midfielder",
                 best_foot="Right",
                 preferred_number=10,
                 birthday="1993-07-10")
    p29.save()

    p30 = Player(full_name="André Filipe Luz Horta",
                 name="André Horta",
                 height=1.75,
                 nationality="Portuguese",
                 position="Central Midfielder",
                 best_foot="Right",
                 preferred_number=8,
                 birthday="1996-11-07")
    p30.save()

    p31 = Player(full_name="Ricardo Jorge Luz Horta",
                 name="Ricardo Horta",
                 height=1.73,
                 nationality="Portuguese",
                 position="Left Winger",
                 best_foot="Right",
                 preferred_number=21,
                 birthday="1994-09-15")
    p31.save()

    p32 = Player(full_name="Tiago Magalhães de Sá",
                 name="Tiago Sá",
                 height=1.85,
                 nationality="Portuguese",
                 position="Goalkeeper",
                 best_foot="Right",
                 preferred_number=1,
                 birthday="1995-01-11")
    p32.save()

    s1 = Staff(name="Aurélio Pereira",
               full_name="Aurélio da Silva Pereira",
               birthday="1947-10-01",
               nationality="Portuguese",
               function="Scout")
    s1.save()

    s2 = Staff(name="Rúben Amorim",
               full_name="Rúben Filipe Marques Amorim",
               birthday="1985-01-27",
               nationality="Portuguese",
               function="Manager")
    s2.save()
    s3 = Staff(name="Frederico Varandas",
               full_name="Frederico Nuno Faro Varandas",
               birthday="1979-09-19",
               nationality="Portuguese",
               function="President")
    s3.save()
    s4 = Staff(name="Hugo Viana",
               full_name="Hugo Miguel Ferreira Gomes Viana",
               birthday="1983-01-15",
               nationality="Portuguese",
               function="Football Director")
    s4.save()
    s5 = Staff(name="Sérgio Conceição",
               full_name="Sérgio Paulo Marceneiro Conceição",
               birthday="1974-11-15",
               nationality="Portuguese",
               function="Manager")
    s5.save()
    s6 = Staff(name="Siramana Dembelé",
               full_name="Siramana Dembelé",
               birthday="1977-01-27",
               nationality="French",
               function="Assistant Manager")
    s6.save()
    s7 = Staff(name="Pinto da Costa",
               full_name="Jorge Nuno de Lima Pinto da Costa",
               birthday="1937-12-28",
               nationality="Portuguese",
               function="President")
    s7.save()
    s8 = Staff(name="Vítor Baía",
               full_name="Vítor Manuel Martins Baía",
               birthday="1969-10-15",
               nationality="Portuguese",
               function="Vice-President")
    s8.save()
    s9 = Staff(name="Jorge Jesus",
               full_name="Jorge Fernando Pinheiro de Jesus",
               birthday="1954-07-24",
               nationality="Portuguese",
               function="Manager")
    s9.save()
    s10 = Staff(name="Pedro Ferreira",
                full_name="Pedro Miguel Carneiro Ferreira",
                birthday="1982-08-11",
                nationality="Portuguese",
                function="Scout")
    s10.save()
    s11 = Staff(name="Luís Filipe Vieira",
                full_name="Luís Filipe Ferreira Vieira",
                birthday="1949-06-22",
                nationality="Portuguese",
                function="President")
    s11.save()
    s12 = Staff(name="Rui Costa",
                full_name="Rui Manuel César Costa",
                birthday="1972-03-29",
                nationality="Portuguese",
                function="Football Director")
    s12.save()
    s13 = Staff(name="Alan",
                full_name="Alan Osório da Costa Silva",
                birthday="1979-09-01",
                nationality="Brazilian",
                function="Director")
    s13.save()

    s14 = Staff(name="Carlos Carvalhal",
                full_name="Carlos Augusto Soares da Costa Faria Carvalhal",
                birthday="1965-12-04",
                nationality="Portuguese",
                function="Manager")
    s14.save()

    s15 = Staff(name="António Salvador",
                full_name="António Salvador da Costa Rodrigues",
                birthday="1970-12-29",
                nationality="Portuguese",
                function="President")
    s15.save()

    s16 = Staff(name="Paulo Meneses",
                full_name="Paulo Meneses",
                birthday="1972-11-13",
                nationality="Portuguese",
                function="Scout")
    s16.save()

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

    cpf = ClubPlaysIn(competition=c, team=t5, season="2020-2021")
    cpf.save()

    cpf = ClubPlaysIn(competition=c, team=t6, season="2020-2021")
    cpf.save()

    cpf = ClubPlaysIn(competition=c, team=t7, season="2020-2021")
    cpf.save()

    cpf = ClubPlaysIn(competition=c, team=t8, season="2020-2021")
    cpf.save()

    cpf = ClubPlaysIn(competition=c, team=t9, season="2020-2021")
    cpf.save()

    cpf = ClubPlaysIn(competition=c, team=t10, season="2020-2021")
    cpf.save()

    cpf = ClubPlaysIn(competition=c, team=t11, season="2020-2021")
    cpf.save()

    cpf = ClubPlaysIn(competition=c, team=t12, season="2020-2021")
    cpf.save()

    cpf = ClubPlaysIn(competition=c, team=t13, season="2020-2021")
    cpf.save()

    cpf = ClubPlaysIn(competition=c, team=t14, season="2020-2021")
    cpf.save()

    cpf = ClubPlaysIn(competition=c, team=t15, season="2020-2021")
    cpf.save()

    cpf = ClubPlaysIn(competition=c, team=t16, season="2020-2021")
    cpf.save()

    cpf = ClubPlaysIn(competition=c, team=t17, season="2020-2021")
    cpf.save()

    cpf = ClubPlaysIn(competition=c, team=t18, season="2020-2021")
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
    try:
        t_parms = {
            'match': Match.objects.get(id=id),
            'comments': CommentMatch.objects.get(match_id=id)
        }
        return render(request, 'match_details.html', t_parms)
    except:
        return error_render(request, 404, "Match not Found")


# Competition Related:

def competitions(request):
    p1 = Player(full_name="Diogo António Cupido Gonçalves", name="Diogo Gonçalves", height=1.78,
                nationality="Portuguese", position="Right Back", best_foot="Right", preferred_number=17)
    p1.save()

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
        if not request.user.is_authenticated:
            return redirect('/login')
        if request.user.username == 'admin':
            if 'delete' in request.POST:
                s = Competition.objects.get(id=id)
                s.delete()
                print("Deleted")
                return redirect(reverse('competitions'))
            else:
                return redirect('/login')
        else:
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

    if not request.user.is_authenticated:
        favouritecompetition = False
        deleteeditbbt = False
    else:
        if request.user.username == 'admin':
            deleteeditbbt = True
            favouritecompetition = False
        else:
            normal = NormalUser.objects.get(user__username=request.user.username)
            if FavouriteCompetition.objects.filter(competition_id=id, user_id=normal.id):
                favouritecompetition = True
                print("Está nos Favoritos")
            else:
                favouritecompetition = False
                print("Não está nos Favoritos")
            deleteeditbbt = False
    try:
        t_parms = {
            'competition': Competition.objects.get(id=id),
            'table': table,
            'teams': teams,
            'season': season,
            'favouritecompetition': favouritecompetition,
            'formComment': MakeCommentForm(),
            'comments': CommentCompetition.objects.filter(competition_id=id),
            'matches': Match.objects.filter(competitionsmatches__competition_id=id, competitionsmatches__season=season),
            'seasons': ClubPlaysIn.objects.filter(competition_id=id).values_list('season', flat=True).distinct(),
            'deleteeditbbt': deleteeditbbt
        }

        return render(request, 'competition_details.html', t_parms)
    except:
        return error_render(request, 404, "Competition not Found")


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
        if not request.user.is_authenticated:
            return redirect('/login')
        if request.user.username == 'admin':
            if 'delete' in request.POST:
                s = Team.objects.get(id=id)
                s.delete()
                print("Deleted")
                return redirect(reverse('teams'))
            else:
                return redirect('/login')
        else:
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

    if not request.user.is_authenticated:
        favouriteteam = False
        deleteeditbbt = False
    else:
        if request.user.username == 'admin':
            favouriteteam = False
            deleteeditbbt = True
        else:
            normal = NormalUser.objects.get(user__username=request.user.username)
            if FavouriteTeam.objects.filter(team_id=id, user_id=normal.id):
                favouriteteam = True
                print("Está nos Favoritos")
            else:
                favouriteteam = False
                print("Não está nos Favoritos")
            deleteeditbbt = False
    try:
        t_parms = {
            'team': Team.objects.get(id=id),
            'competitions': Competition.objects.filter(clubplaysin__team_id=id, clubplaysin__season=season),
            'players': Player.objects.filter(playerplaysfor__team_id=id, playerplaysfor__season=season),
            'seasons': ClubPlaysIn.objects.filter(team_id=id).values_list('season', flat=True).distinct(),
            'staff': StaffManages.objects.filter(team_id=id),
            'comments': CommentTeam.objects.filter(team_id=id),
            'favouriteteam': favouriteteam,
            'formComment': MakeCommentForm(),
            'deleteeditbbt': deleteeditbbt
        }
        return render(request, 'team_details.html', t_parms)
    except:
        return error_render(request, 404, "Team not Found")


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
        deleteeditbbt = False
    else:
        if request.user.username == 'admin':
            deleteeditbbt = True
            favouriteplayer = False
        else:
            normal = NormalUser.objects.get(user__username=request.user.username)
            if FavouritePlayer.objects.filter(player_id=id, user_id=normal.id):
                favouriteplayer = True
                print("Está nos Favoritos")
            else:
                favouriteplayer = False
                print("Não está nos Favoritos")
            deleteeditbbt = False
    try:
        t_parms = {
            'player': Player.objects.get(id=id),
            'teams': set(Team.objects.filter(playerplaysfor__player_id=id).distinct()),  # TODO: Encontrar melhor solução
            'season': PlayerPlaysFor.objects.filter(player_id=id),
            'comments': CommentPlayer.objects.filter(player_id=id),
            'age': int((datetime.date.today() - Player.objects.get(id=id).birthday).days / 365),
            'favouriteplayer': favouriteplayer,
            'formComment': MakeCommentForm(),
            'deleteeditbbt': deleteeditbbt
        }
        return render(request, 'player_details.html', t_parms)
    except:
        return error_render(request, 404, "Player not Found")


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
                    'staffs': Staff.objects.filter(full_name__contains=full_name, function__contains=function,
                                                   nationality__contains=nationality).order_by(
                        order),
                    'form': StaffFilterForm()
                }
            else:
                t_parms = {
                    'staffs': Staff.objects.filter(full_name__contains=full_name, function__contains=function,
                                                   nationality__contains=nationality),
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
        if not request.user.is_authenticated:
            return redirect('/login')
        if request.user.username == 'admin':
            if 'delete' in request.POST:
                s = Staff.objects.get(id=id)
                s.delete()
                print("Deleted")
                return redirect(reverse('staff'))
            else:
                return redirect('/login')
        else:
            normal = NormalUser.objects.get(user__username=request.user.username)
            print(normal.id)
            form = MakeCommentForm(request.POST)
            if form.is_valid():
                comment = form.cleaned_data['comment']
                CommentStaff(user=NormalUser.objects.get(user__username=request.user.username), comment=comment,
                             staff=Staff.objects.get(id=id)).save()
                return HttpResponseRedirect(str(id))  # render(request, 'player_details.html', t_parms)

    if request.user.username == 'admin':
        deleteeditbbt = True
    else:
        deleteeditbbt = False
    try:
        t_parms = {
            'staff': Staff.objects.get(id=id),
            'teams': Team.objects.filter(staffmanages__staff_id=id),
            'seasons': StaffManages.objects.filter(staff_id=id),
            'age': int((datetime.date.today() - Staff.objects.get(id=id).birthday).days / 365),
            'formComment': MakeCommentForm(),
            'comments': CommentStaff.objects.filter(staff_id=id),
            'deleteeditbbt': deleteeditbbt
        }
        return render(request, 'staff_details.html', t_parms)
    except:
        return error_render(request, 404, "Staff not Found")


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
        if request.user.username == 'admin':
            t_parms = {
                'userInfo': User.objects.get(username=request.user.username),
                'check': False
            }
        else:
            t_parms = {
                'userInfo': NormalUser.objects.get(user__username=request.user.username),
                'favouriteTeams': Team.objects.filter(favouriteteam__user__user_id=request.user.id),
                'favouritePlayers': Player.objects.filter(favouriteplayer__user__user_id=request.user.id),
                'favouriteCompetition': Competition.objects.filter(favouritecompetition__user__user_id=request.user.id),
                'check': True
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


def user_verification_insert_edit(request):
    if not request.user.is_authenticated:
        print("lol")
        return redirect('/login')
    if request.user.username != 'admin':
        return error_render(request, 403, "User not allowed")
    return None


# TODO: Meter os edit e os inserts que faltam !!!!!!!!!!!!!
def insert_team(request):
    if user_verification_insert_edit(request) is not None:
        return user_verification_insert_edit(request)
    if request.method == "POST":
        form = InsertTeamForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(
                reverse('teams'))  # return render(request, "insert_all.html", {"form": form, "title": "Team"})
        else:
            print(form.errors)
            return render(request, "insert_all.html", {"form": form, "title": "Team"})
    form = InsertTeamForm()
    return render(request, "insert_all.html", {"form": form, "title": "Team"})


def insert_staff(request):
    if user_verification_insert_edit(request) is not None:
        return user_verification_insert_edit(request)
    if request.method == "POST":
        form = InsertStaffForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(
                reverse('staff'))  # return render(request, "insert_all.html", {"form": form, "title": "Staff"})
        else:
            print(form.errors)
            return render(request, "insert_all.html", {"form": form, "title": "Staff"})
    form = InsertStaffForm()
    return render(request, "insert_all.html", {"form": form, "title": "Staff"})


def insert_player(request):
    if user_verification_insert_edit(request) is not None:
        return user_verification_insert_edit(request)
    if request.method == "POST":
        form = InsertPlayerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('players'))  # render(request, "insert_all.html", {"form": form, "title": "Player"})
        else:
            print(form.errors)
            return render(request, "insert_all.html", {"form": form, "title": "Player"})
    form = InsertPlayerForm()
    return render(request, "insert_all.html", {"form": form, "title": "Player"})


def insert_competition(request):
    if user_verification_insert_edit(request) is not None:
        return user_verification_insert_edit(request)
    if request.method == "POST":
        print(request.FILES)
        form = InsertCompetitionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(
                reverse('competitions'))  # render(request, "insert_all.html", {"form": form, "title": "Competition"})
        else:
            print(form.errors)
            return render(request, "insert_all.html", {"form": form, "title": "Competition"})
    form = InsertCompetitionForm()
    return render(request, "insert_all.html", {"form": form, "title": "Competition"})


def insert_match(request):
    if user_verification_insert_edit(request) is not None:
        return user_verification_insert_edit(request)
    if request.method == "POST":
        form = InsertMatchForm(request.POST)
        if form.is_valid():
            match = form.save(commit=False)
            season = form.cleaned_data["season"]

            home_team = ClubPlaysIn.objects.filter(competition=match.competition, team=match.home_team, season=season)
            away_team = ClubPlaysIn.objects.filter(competition=match.competition, team=match.away_team, season=season)

            if len(home_team) < 1 or len(away_team) < 1:
                print("jogo inválido")
                # página de erro talvez?
                return render(request, "insert_all.html", {"form": form, "title": "Match",
                                                           "error": "One of the teams is not in this Competition"})
            match.save()
            cm = CompetitionsMatches(competition=match.competition, match=match, season=season)
            cm.save()
            return redirect(
                reverse('competitions'))  # render(request, "insert_all.html", {"form": form, "title": "Competition"})
        else:
            print(form.errors)
            return render(request, "insert_all.html", {"form": form, "title": "Match"})
    form = InsertMatchForm()
    return render(request, "insert_all.html", {"form": form, "title": "Match"})



def insert_match_compid(request, compid):
    if user_verification_insert_edit(request) is not None:
        return user_verification_insert_edit(request)
    if request.method == "POST":
        form = InsertMatchForm(request.POST)
        if form.is_valid():
            match = form.save(commit=False)
            season = form.cleaned_data["season"]

            home_team = ClubPlaysIn.objects.filter(competition=match.competition, team=match.home_team, season=season)
            away_team = ClubPlaysIn.objects.filter(competition=match.competition, team=match.away_team, season=season)

            if len(home_team) < 1 or len(away_team) < 1:
                print("jogo inválido")
                # página de erro talvez?
                return render(request, "insert_all.html", {"form": form, "title": "Match",
                                                           "error": "One of the teams is not in this Competition"})
            match.save()
            cm = CompetitionsMatches(competition=match.competition, match=match, season=season)
            cm.save()
            return redirect(reverse('competitions'))#render(request, "insert_all.html", {"form": form, "title": "Competition"})
        else:
            print(form.errors)
            return render(request, "insert_all.html", {"form": form, "title": "Match"})
    try:
        competition = Competition.objects.get(id=compid)
        form = InsertMatchForm(initial={"competition": competition})
        return render(request, "insert_all.html", {"form": form, "title": "Match"})
    except:
        return error_render(request, 404, "Invalid Competition to add Match too")


def insert_team_in_competition(request, compid, season):
    if user_verification_insert_edit(request) is not None:
        return user_verification_insert_edit(request)
    if request.method == "POST":
        form = InsertClubPlaysInForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(
                reverse('competitions'))  # render(request, "insert_all.html", {"form": form, "title": "Competition"})
        else:
            print(form.errors)
            return render(request, "insert_all.html", {"form": form, "title": "Team in Competition"})
    try:
        competition = Competition.objects.get(id=compid)
        form = InsertClubPlaysInForm(initial={"competition": competition, "season": season})
        return render(request, "insert_all.html", {"form": form, "title": "Team in Competition"})
    except:
        return error_render(request, 404, "Invalid Team to add staff too")


def insert_player_in_team(request, teamid):
    if user_verification_insert_edit(request) is not None:
        return user_verification_insert_edit(request)
    if request.method == "POST":
        form = InsertPlayerPlaysForForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(
                reverse('competitions'))  # render(request, "insert_all.html", {"form": form, "title": "Competition"})
        else:
            print(form.errors)
            return render(request, "insert_all.html", {"form": form, "title": "Player in Team"})
    try:
        team = Team.objects.get(id=teamid)
        form = InsertPlayerPlaysForForm(initial={"team": team})
        return render(request, "insert_all.html", {"form": form, "title": "Player in Team"})
    except:
        return error_render(request, 404, "Invalid Team to add staff to")


def insert_staff_in_team(request, teamid):
    if user_verification_insert_edit(request) is not None:
        return user_verification_insert_edit(request)
    if request.method == "POST":
        form = InsertStaffManagesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(
                reverse('competitions'))  # render(request, "insert_all.html", {"form": form, "title": "Competition"})
        else:
            print(form.errors)
            return render(request, "insert_all.html", {"form": form, "title": "Staff in Team"})
    try:
        team = Team.objects.get(id=teamid)
        form = InsertStaffManagesForm(initial={"team": team})
        return render(request, "insert_all.html", {"form": form, "title": "Staff in Team"})
    except:
        return error_render(request, 404, "Invalid Team to add staff too")


def edit_team(request, id):
    if user_verification_insert_edit(request) is not None:
        return user_verification_insert_edit(request)
    if request.method == "POST":
        form = InsertTeamForm(request.POST, request.FILES, instance=Team.objects.get(id=id))
        if form.is_valid():
            form.save()
            return redirect('team_details',
                            str(id))  # return render(request, "edit_all.html", {"form": form, "title": "Team"})
        else:
            print(form.errors)
            return render(request, "edit_all.html", {"form": form, "title": "Team"})
    try:
        team = Team.objects.get(id=id)
        form = InsertTeamForm(instance=team)
        return render(request, "edit_all.html", {"form": form, "title": "Team"})
    except:
        return error_render(request, 404, "Invalid team to edit")


def edit_staff(request, id):
    if user_verification_insert_edit(request) is not None:
        return user_verification_insert_edit(request)
    if request.method == "POST":
        form = InsertStaffForm(request.POST, request.FILES, instance=Staff.objects.get(id=id))
        if form.is_valid():
            form.save()
            return redirect('staff_details',
                            str(id))  # render(request, "edit_all.html", {"form": form, "title": "Staff"})
        else:
            print(form.errors)
            return render(request, "edit_all.html", {"form": form, "title": "Staff"})
    try:
        staff = Staff.objects.get(id=id)
        form = InsertStaffForm(instance=staff)
        return render(request, "edit_all.html", {"form": form, "title": "Staff"})
    except:
        return error_render(request, 404, "Staff not Found")


def edit_player(request, id):
    if user_verification_insert_edit(request) is not None:
        return user_verification_insert_edit(request)
    if request.method == "POST":
        form = InsertPlayerForm(request.POST, request.FILES, instance=Player.objects.get(id=id))
        if form.is_valid():
            form.save()
            return redirect('player_details',
                            str(id))  # render(request, "edit_all.html", {"form": form, "title": "Player"})
        else:
            print(form.errors)
            return render(request, "edit_all.html", {"form": form, "title": "Player"})
    try:
        player = Player.objects.get(id=id)
        form = InsertPlayerForm(instance=player)
        return render(request, "edit_all.html", {"form": form, "title": "Player"})
    except:
        return error_render(request, 404, "Player not Found")


def edit_competition(request, id):
    if user_verification_insert_edit(request) is not None:
        return user_verification_insert_edit(request)
    if request.method == "POST":
        form = InsertCompetitionForm(request.POST, request.FILES, instance=Competition.objects.get(id=id))
        if form.is_valid():
            form.save()
            return redirect('competition_details',
                            str(id))  # render(request, "edit_all.html", {"form": form, "title": "Competition"})
        else:
            print(form.errors)
            return render(request, "edit_all.html", {"form": form, "title": "Competition"})
    try:
        comp = Competition.objects.get(id=id)
        form = InsertCompetitionForm(instance=comp)
        return render(request, "edit_all.html", {"form": form, "title": "Competition"})
    except:
        return error_render(request, 404, "Competition not Found")


def edit_match(request, id):
    if user_verification_insert_edit(request) is not None:
        return user_verification_insert_edit(request)
    if request.method == "POST":
        form = InsertMatchForm(request.POST)
        if form.is_valid():
            cm = CompetitionsMatches.objects.get(match_id=id)
            match = form.save(commit=False)
            season = form.cleaned_data["season"]

            home_team = ClubPlaysIn.objects.filter(competition=match.competition, team=match.home_team, season=season)
            away_team = ClubPlaysIn.objects.filter(competition=match.competition, team=match.away_team, season=season)

            if len(home_team) < 0 or len(away_team) < 0:
                print("jogo inválido")
                #página de erro talvez?
                return render(request, "insert_all.html", {"form": form, "title": "Match",
                                                           "error": "One of the teams is not in this Competition"})
            match.save()
            cm.competition = match.competition
            cm.match = match
            cm.season = form.cleaned_data["season"]
            cm.save()
            return redirect(
                reverse('competitions'))  # render(request, "insert_all.html", {"form": form, "title": "Competition"})
        else:
            return render(request, "edit_all.html", {"form": form, "title": "Match"})
    try:
        match = Match.objects.get(id=id)
        season = CompetitionsMatches.objects.get(match_id=id).season
        form = InsertMatchForm(instance=match, season=season)
        return render(request, "edit_all.html", {"form": form, "title": "Match"})
    except:
        return error_render(request, 404, "Match not Found")
