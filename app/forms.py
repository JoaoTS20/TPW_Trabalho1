from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django.contrib.auth.models import User

from app.models import Team, Player, Staff, ClubPlaysIn, StaffManages, PlayerPlaysFor, CompetitionsMatches, Match


class PlayerFilterForm(forms.Form):
    CHOICES = (
        ('', 'Order By'),
        ('birthday', ' Birthday'),
        ('full_name', 'Full Name'),
        ('height', 'Height'),
    )
    POSITION_CHOICES = (
        ('', 'Position'),
        ('Striker', 'ST-Striker'),
        ('Left Winger', 'LW-Left Winger'),
        ('Right Winger', 'RW-Right Winger'),
        ('Central Attacking Midfielder', 'CAM-Central Attacking Midfielder'),
        ('Central Midfielder', 'CM-Central Midfielder'),
        ('Central Defensive Midfielder', 'CDM-Central Defensive Midfielder'),
        ('Left Back', 'LB-Left Back'),
        ('Right Back', 'RB-Right Back'),
        ('Center Back', 'CB-Center Back'),
        ('Goalkeeper', 'GR-Goalkeeper'),
    )
    BEST_FOOT = (('', 'Best Foot'), ('Left', 'L-Left'), ('Right', 'R-Right'), ('Both', 'B-Both'))

    full_name = forms.CharField(label='Search by Name', required=False)
    position = forms.ChoiceField(choices=POSITION_CHOICES, required=False)
    nationality = forms.CharField(label='Search by Nationality', required=False)
    foot = forms.ChoiceField(choices=BEST_FOOT, required=False)
    order = forms.ChoiceField(choices=CHOICES, required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for myField in self.fields:
            if self.fields[myField] != 'order' and self.fields[myField] != 'position' and self.fields[
                myField] != 'foot':
                self.fields[myField].widget.attrs['class'] = "form-control mb-2 mr-sm-2"
                self.fields[myField].widget.attrs['placeholder'] = self.fields[myField].label


class TeamFilterForm(forms.Form):
    CHOICES = (
        ('', 'Order By'),
        ('founding_year', 'Founding Year'),
        ('full_name', 'Full Name'),
    )
    full_name = forms.CharField(label='Search by Name', required=False)
    country = forms.CharField(label='Search by Country', required=False)
    competition = forms.CharField(label='Search by Competition', required=False)
    order = forms.ChoiceField(choices=CHOICES, required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for myField in self.fields:
            if self.fields[myField] != 'order':
                self.fields[myField].widget.attrs['class'] = "form-control mb-2 mr-sm-2"
                self.fields[myField].widget.attrs['placeholder'] = self.fields[myField].label


class CompetitionFilterForm(forms.Form):
    CHOICES = (
        ('', 'Order By'),
        ('region', 'Region'),
        ('full_name', 'Full Name'),
    )
    full_name = forms.CharField(label='Search by Name', required=False)
    region = forms.CharField(label='Search by Region', required=False)
    order = forms.ChoiceField(choices=CHOICES, required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for myField in self.fields:
            if self.fields[myField] != 'order':
                self.fields[myField].widget.attrs['class'] = "form-control mb-2 mr-sm-2"
                self.fields[myField].widget.attrs['placeholder'] = self.fields[myField].label


class StaffFilterForm(forms.Form):
    CHOICES = (
        ('', 'Order By'),
        ('function', 'Function'),
        ('full_name', 'Full Name'),
        ('birthday','Birthday')
    )
    full_name = forms.CharField(label='Search by Name', required=False)
    nationality = forms.CharField(label='Search by Nationality', required=False)
    function = forms.CharField(label='Search by Function', required=False)
    order = forms.ChoiceField(choices=CHOICES, required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for myField in self.fields:
            if self.fields[myField] != 'order':
                self.fields[myField].widget.attrs['class'] = "form-control mb-2 mr-sm-2"
                self.fields[myField].widget.attrs['placeholder'] = self.fields[myField].label


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
