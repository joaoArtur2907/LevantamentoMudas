from django.urls import path
from . import views

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('propriedades/', views.PropriedadesListView.as_view(), name='propriedade-list'),
    path('propriedades/<int:pk>', views.PropriedadesDetailView.as_view(), name='propriedade-detail'),
    path('viveiros/', views.ViveirosListView.as_view(), name='viveiros-list'),
    path('viveiros/<int:pk>', views.ViveirosDetailView.as_view(), name='viveiro-detail'),
    path('propriedade/create', views.PropriedadeCreate.as_view(), name='propriedade-create'),
    path('propriedade/<int:pk>/update', views.PropriedadeUpdate.as_view(), name='propriedade-update'),
    path('propriedade/<int:pk>/delete', views.PropriedadeDelete.as_view(), name='propriedade-delete'),
    path('viveiro/create', views.ViveiroCreate.as_view(), name='viveiro-create'),
    path('viveiro/<int:pk>/update', views.ViveiroUpdate.as_view(), name='viveiro-update'),
    path('viveiro/<int:pk>/delete', views.ViveiroDelete.as_view(), name='viveiro-delete'),
]
