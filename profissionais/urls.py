from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_profissionais, name='listar_profissionais'),
    path('cadastrar/', views.cadastrar_profissional, name='cadastrar_profissional'),
]
