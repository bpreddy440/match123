from .models import Team, Player, PointsTable, Match
from django import forms


class TeamForm(forms.ModelForm):

    class Meta:
        model = Team
        fields = '__all__'


class PlayerForm(forms.ModelForm):

    class Meta:
        model = Player
        fields = '__all__'
        exclude = ('team',)


