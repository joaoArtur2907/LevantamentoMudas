from django.core.exceptions import ValidationError


def validarPositivo(valor):
    if valor < 0:
        raise ValidationError("O Valor deve ser igual ou maior que zero")

def validarPorcentagem(valor):
    if valor < 0 or valor > 100:
        raise ValidationError("O Valor deve ser entre 0 e 100")
