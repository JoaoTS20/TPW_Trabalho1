"""TPW_Trabalho1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path

from app import views
from app.forms import LogInForm

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),

    path('competitions/', views.competitions, name='competitions'),
    path('competitions/<int:id>', views.competition_details, name='competition_details'),
    path('competitions/<int:id>/<str:season>', views.competition_details, name='competition_details_season'),
    path('insertcompetition/', views.insert_competition, name='insert_competition'),
    path('editcompetition/<int:id>/', views.edit_competition, name='edit_competition'),

    path('teams/', views.teams, name='teams'),
    path('teams/<int:id>', views.team_details, name='team_details'),
    path('teams/<int:id>/<str:season>', views.team_details, name='team_details_season'),
    path('insertteam/', views.insert_team, name='insert_team'),
    path('editteam/<int:id>/', views.edit_team, name='edit_team'),

    path('players/', views.players, name='players'),
    path('players/<int:id>', views.player_details, name='player_details'),
    path('insertplayer/', views.insert_player, name='insert_player'),
    path('editplayer/<int:id>/', views.edit_player, name='edit_player'),

    path('staff/', views.staff, name='staff'),
    path('staff/<int:id>', views.staff_details, name='staff_details'),
    path('insertstaff/', views.insert_staff, name='insert_staff'),
    path('editstaff/<int:id>/', views.edit_staff, name='edit_staff'),

    path('match/<int:id>',views.match_details, name='match_details'),
    path('insertmatch/',views.insert_match, name='insert_match'),

    path('layoutest/', views.test, name='teste'),


    path('login/', auth_views.LoginView.as_view(template_name= 'login.html', authentication_form=LogInForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('signup/', views.signup, name='sign_up'),
    path('profile/', views.profile, name='profile')

]
