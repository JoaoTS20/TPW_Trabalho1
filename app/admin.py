from django.contrib import admin
from app.models import Player, Staff, Team, Competition, Match, ClubPlaysIn,  PlayerPlaysFor, \
    CompetitionsMatches, NormalUser, FavouritePlayer, FavouriteTeam, FavouriteCompetition, CommentPlayer, \
    CommentCompetition, CommentMatch, StaffManages

# Register your models here.
admin.site.register(Player)
admin.site.register(Staff)
admin.site.register(Team)
admin.site.register(Competition)
admin.site.register(Match)
admin.site.register(ClubPlaysIn)
admin.site.register(StaffManages)
admin.site.register(PlayerPlaysFor)
admin.site.register(CompetitionsMatches)
admin.site.register(NormalUser)
admin.site.register(FavouriteTeam)
admin.site.register(FavouritePlayer)
admin.site.register(FavouriteCompetition)
admin.site.register(CommentMatch)
admin.site.register(CommentPlayer)
admin.site.register(CommentCompetition)



