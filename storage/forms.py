from django import forms
from .models import Edinica, Sklads, Etazh, Kabinet

class EdinicaForm(forms.ModelForm):
    class Meta:
        model = Edinica
        fields = '__all__'


