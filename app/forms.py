from django import forms


# Aqui depois mudar option alguns
class TeamFilterForm(forms.Form):
    full_name = forms.CharField(label='Search by Name:', required=False)
    country = forms.CharField(label='Search by Country:', required=False)
    competition = forms.CharField(label='Search by Competition:', required=False)
