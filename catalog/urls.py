from django.urls import path
from . import views

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    # propriedade
    path('propriedades/<int:pk>', views.PropriedadesDetailView.as_view(), name='propriedade-detail'),
    path('propriedades/', views.PropriedadesListView.as_view(), name='propriedade-list'),
    path('propriedade/create', views.PropriedadeCreate.as_view(), name='propriedade-create'),
    path('propriedade/<int:pk>/delete', views.PropriedadeDelete.as_view(), name='propriedade-delete'),
    path('propriedade/<int:pk>/update', views.PropriedadeUpdate.as_view(), name='propriedade-update'),

    # viveiros
    path('viveiros/', views.ViveirosListView.as_view(), name='viveiros-list'),
    path('viveiros/<int:pk>', views.ViveirosDetailView.as_view(), name='viveiro-detail'),
    path('viveiro/create', views.ViveiroCreate.as_view(), name='viveiro-create'),
    path('viveiro/<int:pk>/update', views.ViveiroUpdate.as_view(), name='viveiro-update'),
    path('viveiro/<int:pk>/delete', views.ViveiroDelete.as_view(), name='viveiro-delete'),

    # historico Viveiro
    path('viveiro/<int:viveiro_id>/historico/create', views.HistoricoViveiroCreate.as_view(), name='historicoViveiro-create'),
    path('historicoViveiro/<int:pk>/update', views.HistoricoViveiroUpdate.as_view(), name='historicoViveiro-update'),
    # path('viveiro/<int:viveiro_id>/<int:pk>/historico/update', views.HistoricoViveiroUpdate.as_view(), name='historicoViveiro-update'),
    path('historicoViveiro/<int:pk>/delete', views.HistoricoViveiroDelete.as_view(), name='historicoViveiro-delete'),

    # historico Propriedade
    path('propriedade/<int:propriedade_id>/historico/create', views.HistoricoPropriedadeCreate.as_view(), name='historicoPropriedade-create'),
    path('historicoPropriedade/<int:pk>/update', views.HistoricoPropriedadeUpdate.as_view(), name='historicoPropriedade-update'),
    path('historicoPropriedade/<int:pk>/delete', views.HistoricoPropriedadeDelete.as_view(), name='historicoPropriedade-delete'),

]
