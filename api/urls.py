
from django.urls import path

from . import views

app_name = 'api'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:team_id>/', views.teamdetails, name='teamdetails'),
    path('<int:team_id>/createplayer/', views.createplayerform, name='createplayer'),
    path('<int:team_id>/teamplayers/', views.teamplayers, name='teamplayers'),
    path('<int:team_id>/teamplayers/<int:player_id>/', views.playerdetails, name='playerdetails'),

    path('creatematch/', views.create_match, name='creatematch'),
    path('scorecard/', views.score_card, name='scorecard'),
    path('highscore/', views.highscores, name='highscore'),
]
