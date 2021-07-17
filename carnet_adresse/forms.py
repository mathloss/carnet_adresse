from django import forms
from . models import Adresse

class AdresseFormulaire(forms.ModelForm):
	class Meta:
		model = Adresse
		fields = ["nom", "email", "adresse", "ville", "code_postal", "telephone",]