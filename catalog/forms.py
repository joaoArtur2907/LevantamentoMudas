from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

from catalog.models import HistoricoViveiro, HistoricoPropriedade


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email')

class UserLoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','email', 'password')

class HistoricoViveiroForm(forms.ModelForm):
    class Meta:
        model = HistoricoViveiro
        fields = '__all__'
        widgets = {
            'cultivar': forms.CheckboxSelectMultiple(),
            'sistemasDeProducao': forms.CheckboxSelectMultiple(),
        }

class HistoricoPropriedadeForm(forms.ModelForm):
    class Meta:
        model = HistoricoPropriedade
        fields = '__all__'
        widgets = {
            'cultivar': forms.CheckboxSelectMultiple(),
            'sistemasDeProducao': forms.CheckboxSelectMultiple(),
        }
