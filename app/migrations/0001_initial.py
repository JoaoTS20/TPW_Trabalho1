# Generated by Django 3.2 on 2021-04-29 11:14

import app.models
import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ClubPlaysIn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('season', models.CharField(max_length=9, validators=[django.core.validators.RegexValidator(code='invalid_season', message='Season must follow the format year-year', regex='[0-9]{4}-[0-9]{4}')])),
            ],
        ),
        migrations.CreateModel(
            name='Competition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=70)),
                ('competition_badge_img', models.ImageField(default='competitions/default_league.png', upload_to=app.models.compdir)),
                ('region', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='FavouriteCompetition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('competition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.competition')),
            ],
        ),
        migrations.CreateModel(
            name='FavouritePlayer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='FavouriteTeam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=120)),
                ('name', models.CharField(max_length=90)),
                ('birthday', models.DateField()),
                ('height', models.FloatField(validators=[django.core.validators.MinValueValidator(0)])),
                ('nationality', models.CharField(max_length=70)),
                ('position', models.CharField(choices=[('Striker', 'ST-Striker'), ('Left Winger', 'LW-Left Winger'), ('Right Winger', 'RW-Right Winger'), ('Central Attacking Midfielder', 'CAM-Central Attacking Midfielder'), ('Central Midfielder', 'CM-Central Midfielder'), ('Central Defensive Midfielder', 'CDM-Central Defensive Midfielder'), ('Left Back', 'LB-Left Back'), ('Right Back', 'RB-Right Back'), ('Center Back', 'CB-Center Back'), ('Goalkeeper', 'GR-Goalkeeper')], max_length=28)),
                ('best_foot', models.CharField(choices=[('Left', 'L-Left'), ('Right', 'R-Right'), ('Both', 'B-Both')], max_length=5)),
                ('preferred_number', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)])),
                ('player_img', models.ImageField(default='players/default_player.png', upload_to=app.models.playerdir)),
            ],
        ),
        migrations.CreateModel(
            name='PlayerPlaysFor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('season', models.CharField(max_length=9, validators=[django.core.validators.RegexValidator(code='invalid_season', message='Season must follow the format year-year', regex='[0-9]{4}-[0-9]{4}')])),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.player')),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=120)),
                ('name', models.CharField(max_length=90)),
                ('birthday', models.DateField()),
                ('nationality', models.CharField(max_length=70)),
                ('function', models.CharField(max_length=70)),
                ('staff_img', models.ImageField(default='staff/default_staff.png', upload_to=app.models.staffdir)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=70)),
                ('name', models.CharField(max_length=70)),
                ('abreviated_name', models.CharField(max_length=4)),
                ('founding_year', models.IntegerField()),
                ('club_badge_img', models.ImageField(default='teams/default_club.png', upload_to=app.models.teamdir)),
                ('city', models.CharField(max_length=20)),
                ('country', models.CharField(max_length=20)),
                ('formation', models.CharField(max_length=5, validators=[django.core.validators.RegexValidator(code='invalid_formation', message='Season must follow the format number-number-number', regex='[0-9]{1}-[0-9]{1}-[0-9]{1}')])),
                ('players', models.ManyToManyField(through='app.PlayerPlaysFor', to='app.Player')),
            ],
        ),
        migrations.CreateModel(
            name='StaffManages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('season', models.CharField(max_length=9, validators=[django.core.validators.RegexValidator(code='invalid_season', message='Season must follow the format year-year', regex='[0-9]{4}-[0-9]{4}')])),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.staff')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.team')),
            ],
        ),
        migrations.AddField(
            model_name='playerplaysfor',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.team'),
        ),
        migrations.CreateModel(
            name='NormalUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_football_related', models.BooleanField()),
                ('favouritecompetitions', models.ManyToManyField(through='app.FavouriteCompetition', to='app.Competition')),
                ('favouriteplayers', models.ManyToManyField(through='app.FavouritePlayer', to='app.Player')),
                ('favouriteteams', models.ManyToManyField(through='app.FavouriteTeam', to='app.Team')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ngame', models.IntegerField()),
                ('description', models.CharField(max_length=25)),
                ('home_goals', models.PositiveIntegerField()),
                ('away_goals', models.PositiveIntegerField()),
                ('away_team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='away_team', to='app.team')),
                ('competition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.competition')),
                ('home_team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='home_team', to='app.team')),
            ],
        ),
        migrations.AddField(
            model_name='favouriteteam',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.team'),
        ),
        migrations.AddField(
            model_name='favouriteteam',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.normaluser'),
        ),
        migrations.AddField(
            model_name='favouriteplayer',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.player'),
        ),
        migrations.AddField(
            model_name='favouriteplayer',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.normaluser'),
        ),
        migrations.AddField(
            model_name='favouritecompetition',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.normaluser'),
        ),
        migrations.CreateModel(
            name='CompetitionsMatches',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('season', models.CharField(max_length=9, validators=[django.core.validators.RegexValidator(code='invalid_season', message='Season must follow the format year-year', regex='[0-9]{4}-[0-9]{4}')])),
                ('competition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.competition')),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.match')),
            ],
        ),
        migrations.AddField(
            model_name='competition',
            name='teams',
            field=models.ManyToManyField(through='app.ClubPlaysIn', to='app.Team'),
        ),
        migrations.CreateModel(
            name='CommentTeam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timeofpost', models.DateTimeField(default=datetime.datetime.now)),
                ('comment', models.CharField(max_length=120)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.team')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.normaluser')),
            ],
        ),
        migrations.CreateModel(
            name='CommentStaff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timeofpost', models.DateTimeField(default=datetime.datetime.now)),
                ('comment', models.CharField(max_length=120)),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.staff')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.normaluser')),
            ],
        ),
        migrations.CreateModel(
            name='CommentPlayer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timeofpost', models.DateTimeField(default=datetime.datetime.now)),
                ('comment', models.CharField(max_length=120)),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.player')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.normaluser')),
            ],
        ),
        migrations.CreateModel(
            name='CommentMatch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timeofpost', models.DateTimeField(default=datetime.datetime.now)),
                ('comment', models.CharField(max_length=120)),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.match')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.normaluser')),
            ],
        ),
        migrations.CreateModel(
            name='CommentCompetition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timeofpost', models.DateTimeField(default=datetime.datetime.now)),
                ('comment', models.CharField(max_length=120)),
                ('competition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.competition')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.normaluser')),
            ],
        ),
        migrations.AddField(
            model_name='clubplaysin',
            name='competition',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.competition'),
        ),
        migrations.AddField(
            model_name='clubplaysin',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.team'),
        ),
    ]
