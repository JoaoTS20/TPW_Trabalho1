from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django.contrib.auth.models import User

from app.models import Team, Player, Staff, ClubPlaysIn, StaffManages, PlayerPlaysFor, CompetitionsMatches, Match


class TeamFilterForm(forms.Form):
    full_name = forms.CharField(label='Search by Name:', required=False)
    country = forms.CharField(label='Search by Country:', required=False)
    competition = forms.CharField(label='Search by Competition:', required=False)


class MakeCommentForm(forms.Form):
    comment = forms.CharField(widget=forms.Textarea, label='Add Comment')
    fields = ('comment')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for myField in self.fields:
            self.fields[myField].widget.attrs['rows'] = 3
            self.fields[myField].widget.attrs['class'] = 'form-control'
            self.fields[myField].widget.attrs['style'] = 'resize:none'


class FavouriteForm(forms.Form):
    favouritecheck = forms.CheckboxInput()
    fields = ('favouritecheck')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for myField in self.fields:
            self.fields[myField].widget.attrs['class'] = 'form-check-input'
            self.fields[myField].widget.attrs['type'] = 'checkbox'


class LogInForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=150)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for myField in self.fields:
            if myField != 'job_football_related':
                self.fields[myField].widget.attrs['class'] = 'form-control'
                self.fields[myField].widget.attrs['placeholder'] = self.fields[myField].label


class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="Email Address")
    job_football_related = forms.BooleanField(required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for myField in self.fields:
            if myField != 'job_football_related':
                self.fields[myField].widget.attrs['class'] = 'form-control'
                self.fields[myField].widget.attrs['placeholder'] = self.fields[myField].label

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2", "job_football_related",)


class InsertPlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = "__all__"


class InsertStaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = "__all__"


class InsertTeamForm(forms.ModelForm):
    # specify the name of model to use
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for myField in self.fields:
                self.fields[myField].widget.attrs['class'] = 'form-control'

    class Meta:
        model = Team
        fields = "__all__"


class InsertCompetitionForm(forms.Form):
    full_name = forms.CharField(max_length=70, label="Full Name")
    file = forms.FileField(label="Image", required=False)
    region = forms.CharField(max_length=70, label="Region")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for myField in self.fields:
                self.fields[myField].widget.attrs['class'] = 'form-control'
                self.fields[myField].widget.attrs['placeholder'] = self.fields[myField].label


class InsertMatchForm(forms.ModelForm):
    class Meta:
        model = Match
        fields = "__all__"


class InsertClubPlaysInForm(forms.ModelForm):
    class Meta:
        model = ClubPlaysIn
        fields = "__all__"


class InsertStaffManagesForm(forms.ModelForm):
    class Meta:
        model = StaffManages
        fields = "__all__"


class InsertPlayerPlaysForForm(forms.ModelForm):
    class Meta:
        model = PlayerPlaysFor
        fields = "__all__"


class InsertCompetitionsMatchesForm(forms.ModelForm):
    class Meta:
        model = CompetitionsMatches
        fields = "__all__"
