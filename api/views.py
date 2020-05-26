import random

from django.db.models import Count
from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Team, Match, PointsTable, Player
from .forms import TeamForm, PlayerForm


# Create your views here.


def index(request):
    team_list = Team.objects.all()
    return render(request, 'api/index.html', {'team_list': team_list})


def teamdetails(request, team_id):
    team = get_object_or_404(Team, id=team_id)
    return render(request, 'api/teamdetails.html', {'team': team})


def createplayerform(request, team_id):
    team = get_object_or_404(Team, id=team_id)
    if request.method == "POST":
        form = PlayerForm(request.POST, request.FILES)
        if form.is_valid():
            ply = form.save(commit=False)
            ply.team = team
            ply.save()
            return HttpResponseRedirect(reverse('api:index'))
    form = PlayerForm()
    return render(request, "api/createplayerform.html", {'form': form})


def teamplayers(request, team_id):
    team = get_object_or_404(Team, id=team_id)
    return render(request, 'api/teamplayers.html', {'team': team})


def playerdetails(request, player_id, team_id):

    player = get_object_or_404(Player, id=player_id)
    print(player.firstName)
    return render(request, 'api/playerdetails.html', {'player': player})


def create_match(request):
    teams = Team.objects.all().values_list('name')
    team_list = [team[0] for team in teams]

    print(team_list)
    team1, team2 = random.sample(team_list, 2)
    print(team1, team2)

    if request.method == 'POST':

        match = Match.objects.create(
            team1=team1,
            team2=team2,
            winner=request.POST['winner'],
        )
        PointsTable.objects.create(
            match=match,
            points=request.POST['points'],
            description=request.POST['description'],
        )
        return HttpResponse('winner is : \t' + str(match.winner))
    return render(request, 'api/creatematch.html', {'team1': team1, 'team2': team2})


def score_card(request):
    scorecard = PointsTable.objects.all()
    return render(request, 'api/scorecard.html', {'scorecard': scorecard})


def highscores(request):
    dct={}
    scorecard = PointsTable.objects.all()
    for score in scorecard:
        dct.setdefault(score.match.winner, 0)
        dct[score.match.winner]+=1

    return render(request, 'api/highscores.html', {'scorecard': dct})
