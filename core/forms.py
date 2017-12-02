from django import forms
from .choices import *
from .models import Tcc

class TccForm(forms.ModelForm):

    class Meta:
        model = Tcc
        fields = ('nome','aluno','curso',)
		
class CViewerForm(forms.Form):

    curso = forms.ChoiceField(choices = MY_CHOICES, label="", initial='', widget=forms.Select(), required=True)