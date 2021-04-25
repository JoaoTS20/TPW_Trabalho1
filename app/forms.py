from django import forms
from django.contrib.auth.forms import UserCreationForm

# Aqui depois mudar option alguns
from django.contrib.auth.models import User

from app.models import NormalUser


class TeamFilterForm(forms.Form):
    full_name = forms.CharField(label='Search by Name:', required=False)
    country = forms.CharField(label='Search by Country:', required=False)
    competition = forms.CharField(label='Search by Competition:', required=False)


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
