from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.views.generic import CreateView, UpdateView, DeleteView

from .models import Propriedade, Viveiro, HistoricoViveiro, HistoricoPropriedade, DificuldadeProducao, Cultivar, SistemaProducao

@login_required
def index(request):
    "View function form home page"

    num_Propriedades = Propriedade.objects.all().count()
    num_Viveiros = Viveiro.objects.all().count()
    num_Historicos_Viveiros = HistoricoViveiro.objects.all().count()
    num_Historicos_Propriedades = HistoricoPropriedade.objects.all().count()
    num_Cultivar = Cultivar.objects.all().count()

    num_Historicos_Propriedades_2025 = HistoricoPropriedade.objects.filter(ano=2025).count()
    num_Historicos_Viveiros_2025 = HistoricoViveiro.objects.filter(ano=2025).count()

    context = {
        'num_Propriedades': num_Propriedades,
        'num_Viveiros': num_Viveiros,
        'num_Historicos_Viveiros': num_Historicos_Viveiros,
        'num_Historicos_Propriedades': num_Historicos_Propriedades,
        'num_Cultivar': num_Cultivar,
        'num_Historicos_Propriedades_2025': num_Historicos_Propriedades_2025,
        'num_Historicos_Viveiros_2025': num_Historicos_Viveiros_2025,
    }

    return render(request, 'index.html', context=context)


class PropriedadesListView(LoginRequiredMixin, generic.ListView):
    model = Propriedade
    context_object_name = 'propriedades_list'
    paginate_by = 4


class ViveirosListView(LoginRequiredMixin, generic.ListView):
    model = Viveiro
    context_object_name = 'viveiros_list'
    paginate_by = 4


class PropriedadesDetailView(LoginRequiredMixin, generic.DetailView):
    model = Propriedade



class ViveirosDetailView(LoginRequiredMixin, generic.DetailView):
    model = Viveiro


class PropriedadeCreate(PermissionRequiredMixin, CreateView):
    model = Propriedade
    fields = '__all__'
    initial = {'nome': '<NAME>'}
    permission_required = 'catalog.add_propriedade'

class PropriedadeUpdate(PermissionRequiredMixin, UpdateView):
    model = Propriedade
    fields = '__all__'
    permission_required = 'catalog.change_propriedade'

class PropriedadeDelete(PermissionRequiredMixin, DeleteView):
    model = Propriedade
    success_url = reverse_lazy('propriedade-list')
    permission_required = 'catalog.delete_propriedade'

    def form_valid(self, form):
        try:
            self.object.delete()
            return HttpResponseRedirect(self.success_url)
        except Exception as e:
            return HttpResponseRedirect(
                reverse("propriedade-delete", kwargs={"pk": self.object.id})
            )
# algum erro nesse reverse ai importado talvez

class ViveiroCreate(PermissionRequiredMixin, CreateView):
    model = Viveiro
    fields = '__all__'
    initial = {'nome': '<NAME>'}
    permission_required = 'catalog.add_viveiro'

class ViveiroUpdate(PermissionRequiredMixin, UpdateView):
    model = Viveiro
    fields = '__all__'
    initial = {'nome': '<NAME>'}
    permission_required = 'catalog.change_viveiro'

class ViveiroDelete(PermissionRequiredMixin, DeleteView):
    model = Viveiro
    success_url = reverse_lazy('viveiro-list')
    permission_required = 'catalog.delete_viveiro'

    def form_valid(self, form):
        try:
            self.object.delete()
            return HttpResponseRedirect(self.success_url)
        except Exception as e:
            return HttpResponseRedirect(
                reverse("viveiro-delete", kwargs={"pk": self.object.id})
            )
