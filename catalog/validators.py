from django.core.exceptions import ValidationError


def validarPositivo(valor):
    if valor < 0:
        raise ValidationError("O Valor deve ser igual ou maior que zero")
