from datetime import datetime

from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.db.models import UniqueConstraint
from django.urls import reverse
from django.db.models.functions import Lower

from catalog.validators import validarPositivo, validarPorcentagem


class Propriedade(models.Model):
    """modelo representando a propriedade"""

    responsavel = models.CharField(
        max_length=100,
        help_text='Nome do responsável sobre a propriedade'
    )

    def __str__(self):
        return self.responsavel

    def get_absolute_url(self):
        return reverse('propriedade-detail', args=[str(self.id)])

    localGeo = models.CharField(
        max_length=500,
        help_text='Localização Geográfica da propriedade',
        blank=True, null=True,
        verbose_name='Localização'
    )

    contatoResponsavel = models.CharField(
        max_length=20,
        help_text='Número de telefone do responsável sobre a propriedade',
        blank=True, null=True,
        verbose_name='Telefone'
    )

    morangoAtividadePrincipal = models.BooleanField(
        default=False,
        verbose_name='Morango é a atividade principal da propriedade?'

    )



class Viveiro(models.Model):
    """modelo representando o viveiro"""

    responsavel = models.CharField(
        max_length=100,
        help_text='Nome do responsável sobre o viveiro'
    )

    def __str__(self):
        return self.responsavel

    def get_absolute_url(self):
        return reverse('viveiro-detail', args=[str(self.id)])

    localGeo = models.CharField(
        max_length=500,
        help_text='Localização Geográfica do viveiro',
        blank=True, null=True,
        verbose_name='Localização'
    )

    contatoResponsavel = models.CharField(
        max_length=20,
        help_text='Número de telefone do responsável sobre o viveiro',
        blank=True, null=True,
        verbose_name='Telefone'
    )

    possuiAssistencia = models.BooleanField(
        default=False,
        verbose_name='O viveiro possui assistência?',
        blank=True, null=True,

    )



class DificuldadeProducao(models.Model):
    """modelo representando o dificuldade da producao"""
    nomeDificuldade = models.CharField(
        max_length=100,
        help_text='Tipo de dificuldade da producao',
        blank=True, null=True,
        verbose_name='Tipo de dificuldade',
        unique=True
    )

    def __str__(self):
        return self.nomeDificuldade

    def get_absolute_url(self):
        return reverse('nomeDificuldade', args=[str(self.id)])

    class Meta:
        constraints = [
            UniqueConstraint(
                Lower('nomeDificuldade'),
                name='dificuldade_name_case_insensitive_unique',
                violation_error_message="Dificuldade já existe (case insensitive match)"
            ),
        ]

class Cultivar(models.Model):
    """modelo representando o cultivar"""
    nomeCultivar = models.CharField(
        max_length=100,
        help_text='Nome do cultivar',
        verbose_name='Nome do cultivar',
        unique=True
    )

    def __str__(self):
        return self.nomeCultivar

    def get_absolute_url(self):
        return reverse('cultivar-detail', args=[str(self.id)])


class SistemaProducao(models.Model):
    nome = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nome

class HistoricoPropriedade(models.Model):
    """modelo representando o historico de propriedade"""
    sistemasDeProducao = models.ManyToManyField(SistemaProducao, verbose_name="Sistema de Produção")

    numPlantas = models.IntegerField(
        blank=True, null=True,
        help_text= "Numero de plantas da propriedade",
        verbose_name='Numero de plantas da propriedade',
        validators = [validarPositivo]
    )


    B2B = models.IntegerField(
        blank=True, null=True,
        help_text= "O quanto sua propriedade vende para outras empresas",
        verbose_name="Business to Business",
        validators=[validarPositivo, validarPorcentagem]
    )

    B2C = models.IntegerField(
        blank=True, null=True,
        help_text="O quanto sua propriedade vende diretamente ao público",
        verbose_name="Business to Consumer",
        validators=[validarPositivo, validarPorcentagem]
    )

    ano = models.IntegerField(
        help_text="Ano da resposta",
        verbose_name="Ano da resposta",
        default=datetime.now().year,
        validators=[validarPositivo]
    )

    cultivar = models.ManyToManyField(
        Cultivar, help_text='Cultivares do viveiro'
    )

    propriedade = models.ForeignKey('Propriedade', on_delete=models.CASCADE)

    def __str__(self):
        propriedade_nome = self.propriedade.responsavel if self.propriedade else "Sem propriedade"
        return f"Histórico da propriedade de {propriedade_nome} ({self.ano})"

class HistoricoViveiro(models.Model):
    """modelo representando o historico de propriedade"""

    sistemasDeProducao = models.ManyToManyField(SistemaProducao, verbose_name="Sistema de Produção")

    numPlantas = models.IntegerField(
        blank=True, null=True,
        help_text= "Numero de plantas do viveiro",
        verbose_name='Numero de plantas do viveiro',
        validators=[validarPositivo]
    )

    numClientes = models.IntegerField(
        blank=True, null=True,
        help_text="Numero de clientes do viveiro",
        verbose_name='Numero de clientes do viveiro',
        validators = [validarPositivo]
    )

    B2B = models.IntegerField(
        blank=True, null=True,
        help_text= "O quanto seu viveiro vende para outras empresas",
        verbose_name="Business to Business",
        validators=[validarPositivo, validarPorcentagem]
    )

    B2C = models.IntegerField(
        blank=True, null=True,
        help_text="O quanto seu viveiro vende diretamente ao público",
        verbose_name="Business to Consumer",
        validators=[validarPositivo, validarPorcentagem]
    )

    ano = models.IntegerField(
        help_text="Ano da resposta",
        verbose_name="Ano da resposta",
        default=datetime.now().year,
        validators=[validarPositivo]
    )

    cultivar = models.ManyToManyField(
        Cultivar, help_text='Cultivares do viveiro'
    )

    viveiro = models.ForeignKey('Viveiro', on_delete=models.CASCADE)

    def __str__(self):
        viveiro_nome = self.viveiro.responsavel if self.viveiro else "Sem viveiro"
        return f"Histórico do viveiro de {viveiro_nome} ({self.ano})"




