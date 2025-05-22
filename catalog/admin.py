from django.contrib import admin
from .models import Viveiro, HistoricoViveiro, Propriedade, HistoricoPropriedade, Cultivar,DificuldadeProducao, SistemaProducao

# Register your models here.

admin.site.register(Viveiro)
admin.site.register(HistoricoViveiro)
admin.site.register(Propriedade)
admin.site.register(HistoricoPropriedade)
admin.site.register(Cultivar)
admin.site.register(DificuldadeProducao)
admin.site.register(SistemaProducao)