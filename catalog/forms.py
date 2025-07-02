from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from catalog.models import HistoricoViveiro, HistoricoPropriedade


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email')
        labels = {
            "username": "Nome de usuário",
            "email": "E-mail",
        }

class UserLoginForm(UserCreationForm):
    password1 = forms.CharField(
        label="Senha",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text="Sua senha deve conter pelo menos 8 caracteres e não ser totalmente numérica."
    )
    password2 = forms.CharField(
        label="Confirmação de senha",
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        strip=False,
        help_text="Digite a senha novamente para confirmação."
    )

    class Meta:
        model = User
        fields = ("username", "password1", "password2", "email")
        labels = {
            "username": "Nome de usuário",
            "email": "E-mail",
        }
        help_texts = {
            "username": "Obrigatório. 150 caracteres ou menos. Letras, números e @/./+/-/_ apenas.",
            "email": "Insira seu email",
        }

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
