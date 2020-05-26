from django.contrib import admin

from .models import Team, PointsTable, Match, Player, PlayerHistory
# Register your models here.
admin.site.register(Team)
admin.site.register(Match)
admin.site.register(Player)
admin.site.register(PlayerHistory)
admin.site.register(PointsTable)