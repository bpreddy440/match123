from django.db import models

# Create your models here.


class Team(models.Model):

    name = models.CharField(max_length=50, unique=True)
    identifier = models.CharField(max_length=50, unique=True)
    logoUri = models.FileField(upload_to="media/")
    club_state = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Player(models.Model):

    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    identifier = models.CharField(max_length=50, unique=True)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    imageUri = models.FileField(upload_to="media/")
    Player_jersey_number = models.IntegerField()
    Country = models.CharField(max_length=50)

    def __str__(self):
        return str(self.firstName) + " " + str(self.lastName)


class PlayerHistory(models.Model):
    player = models.OneToOneField(Player, on_delete=models.CASCADE)
    player_record = models.CharField(max_length=50)
    count_50 = models.IntegerField(default=0)
    count_100 = models.IntegerField(default=0)

    def __str__(self):
        return str(self.player)+" player history"


class Match(models.Model):

    # Matches between the teams
    team1 = models.CharField(max_length=50)
    team2 = models.CharField(max_length=50)
    winner = models.CharField(max_length=50)

    def __str__(self):
        return str(self.team1) + "vs" + str(self.team2)


class PointsTable(models.Model):

    match = models.OneToOneField(Match, on_delete=models.CASCADE)
    points = models.IntegerField(default=1)
    description = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return str(self.match) + 'description:'+str(self.description)