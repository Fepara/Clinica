from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_agendamentos, name='listar_agendamentos'),
    path('criar/', views.criar_agendamento, name='criar_agendamento'),
]
