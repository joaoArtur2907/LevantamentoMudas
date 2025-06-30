from mimetypes import inited

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.views.generic import CreateView, UpdateView, DeleteView, ListView

from .forms import UserForm, UserLoginForm
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
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        historicos = self.object.historicopropriedade_set.all()
        paginator = Paginator(historicos, self.paginate_by)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context['historicos_page'] = page_obj
        return context


class ViveirosDetailView(LoginRequiredMixin, generic.DetailView):
    model = Viveiro
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        historicos = self.object.historicoviveiro_set.all()
        paginator = Paginator(historicos, self.paginate_by)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context['historicos_page'] = page_obj
        return context

class PropriedadeCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Propriedade
    fields = '__all__'
    initial = {'nome': '<NAME>'}
    permission_required = 'catalog.add_propriedade'

class PropriedadeUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Propriedade
    fields = '__all__'
    permission_required = 'catalog.change_propriedade'

class PropriedadeDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Propriedade
    success_url = reverse_lazy('propriedade-list')
    permission_required = 'catalog.delete_propriedade'

    def form_valid(self, form):
        try:
            self.object.delete()
            return HttpResponseRedirect(self.success_url)
        except Exception as e:
            return HttpResponseRedirect(
                reverse("propriedade-list")
            )


# algum erro nesse reverse ai importado talvez

class ViveiroCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Viveiro
    fields = '__all__'
    initial = {'nome': '<NAME>'}
    permission_required = 'catalog.add_viveiro'

class ViveiroUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Viveiro
    fields = '__all__'
    initial = {'nome': '<NAME>'}
    permission_required = 'catalog.change_viveiro'

class ViveiroDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Viveiro
    success_url = reverse_lazy('viveiro-list')
    permission_required = 'catalog.delete_viveiro'


    def form_valid(self, form):
        obj_id = self.object.id
        try:
            self.object.delete()
            return HttpResponseRedirect(self.success_url)
        except Exception as e:
            return HttpResponseRedirect(
                reverse("viveiros-list")
            )

class HistoricoViveiroCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = HistoricoViveiro
    fields = '__all__'
    permission_required = 'catalog.add_historico_viveiro'

   #pega o id do viveiro e adiciona diretamente no formulario
    def get_initial(self):
        initial = super().get_initial()
        viveiro_id = self.kwargs.get('viveiro_id')
        if viveiro_id:
            initial['viveiro'] = viveiro_id
        return initial

    # faz o campo viveiro ser readonly
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        viveiro_id = self.kwargs.get('viveiro_id')
        if viveiro_id:
            form.fields['viveiro'].initial = viveiro_id
            form.fields['viveiro'].widget.attrs['readonly'] = True
        return form

    def get_success_url(self):
        return reverse('viveiro-detail', kwargs={'pk': self.object.viveiro.id})


class HistoricoViveiroUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = HistoricoViveiro
    fields = '__all__'
    permission_required = 'catalog.change_historico_viveiro'
    success_url = reverse_lazy('viveiros-list')

    def get_initial(self):
        initial = super().get_initial()
        viveiro_id = self.kwargs.get('viveiro_id')
        if viveiro_id:
            initial['viveiro'] = viveiro_id
        return initial

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        viveiro_id = self.kwargs.get('viveiro_id')
        if viveiro_id:
            form.fields['viveiro'].initial = viveiro_id
            form.fields['viveiro'].widget.attrs['readonly'] = True
        return form

    def get_success_url(self):
        return reverse('viveiro-detail', kwargs={'pk': self.object.viveiro.id})



class HistoricoViveiroDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = HistoricoViveiro
    success_url = reverse_lazy('viveiros-list')
    permission_required = 'catalog.delete_historico_viveiro'

    def form_valid(self, form):
        try:
            self.object.delete()
            return HttpResponseRedirect(self.success_url)
        except Exception as e:
            return HttpResponseRedirect(
                reverse("historico-viveiro-delete", args=[self.object.id])
            )


class HistoricoPropriedadeCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = HistoricoPropriedade
    fields = '__all__'
    permission_required = 'catalog.add_historico_propriedade'

    def get_initial(self):
        initial = super().get_initial()
        propriedade_id = self.kwargs.get('propriedade_id')
        if propriedade_id:
            initial['propriedade'] = propriedade_id
        return initial

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        propriedade_id = self.kwargs.get('propriedade_id')
        if propriedade_id:
            form.fields['propriedade'].initial = propriedade_id
            form.fields['propriedade'].widget.attrs['readonly'] = True
        return form

    def get_success_url(self):
        return reverse('propriedade-detail', kwargs={'pk': self.object.propriedade.id})

class HistoricoPropriedadeUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = HistoricoPropriedade
    fields = '__all__'
    permission_required = 'catalog.change_historico_propriedade'
    success_url = reverse_lazy('propriedades-list')

    def get_initial(self):
        initial = super().get_initial()
        propriedade_id = self.kwargs.get('propriedade_id')
        if propriedade_id:
            initial['propriedade'] = propriedade_id
        return initial

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        propriedade_id = self.kwargs.get('propriedade_id')
        if propriedade_id:
            form.fields['propriedade'].initial = propriedade_id
            form.fields['propriedade'].widget.attrs['readonly'] = True
        return form

    def get_success_url(self):
        return reverse('propriedade-detail', kwargs={'pk': self.object.propriedade.id})


class HistoricoPropriedadeDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = HistoricoPropriedade
    success_url = reverse_lazy('propriedade-list')
    permission_required = 'catalog.delete_historico_propriedade'

    def form_valid(self, form):
        try:
            self.object.delete()
            return HttpResponseRedirect(self.success_url)
        except Exception as e:
            return HttpResponseRedirect(
                reverse("historico-propriedade-delete", args=[self.object.id])
            )
    def get_success_url(self):
        return reverse('propriedade-detail', kwargs={'pk': self.object.propriedade.id})


# usuários

class UserListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = User
    permission_required = 'catalog.view_user'
    context_object_name = 'usuarios'
    template_name = 'catalog/user_list.html'
    paginate_by = 10


class UserCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = User
    initial = {'nome': '<NAME>'}
    permission_required = 'catalog.add_user'
    template_name = 'catalog/User_form.html'
    form_class = UserLoginForm

    def get_success_url(self):
        return reverse('user-list')


class UserUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = User
    initial = {'nome': '<NAME>'}
    permission_required = 'catalog.change_user'
    template_name = 'catalog/User_form.html'
    form_class = UserForm

    def get_success_url(self):
        return reverse('user-list')

class UserDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = User
    success_url = reverse_lazy('user-list')
    permission_required = 'catalog.delete_user'
    template_name = 'catalog/User_confirm_delete.html'


    def form_valid(self, form):
        obj_id = self.object.id
        try:
            self.object.delete()
            return HttpResponseRedirect(self.success_url)
        except Exception as e:
            return HttpResponseRedirect(
                reverse("user-list")
            )