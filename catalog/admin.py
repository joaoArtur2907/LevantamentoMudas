from django.contrib import admin
from . import forms
from .models import Viveiro, HistoricoViveiro, Propriedade, HistoricoPropriedade, Cultivar,DificuldadeProducao, SistemaProducao
from django.db import models
from django.forms import CheckboxSelectMultiple
# Register your models here.

admin.site.register(Viveiro)
admin.site.register(Propriedade)
admin.site.register(Cultivar)
admin.site.register(DificuldadeProducao)
admin.site.register(SistemaProducao)

class BaseCheckbox(admin.ModelAdmin):
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }


admin.site.register(HistoricoViveiro, BaseCheckbox)
admin.site.register(HistoricoPropriedade, BaseCheckbox)
