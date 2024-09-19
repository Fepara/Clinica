from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_atendimentos, name='listar_atendimentos'),
    path('criar/', views.criar_atendimento, name='criar_atendimento'),
]
