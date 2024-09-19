from django.urls import path
from . import views

urlpatterns = [
    path('pagamentos/', views.listar_pagamentos, name='listar_pagamentos'),
    path('pagamentos/criar/', views.criar_pagamento, name='criar_pagamento'),
    
    path('despesas/', views.listar_despesas, name='listar_despesas'),
    path('despesas/criar/', views.criar_despesa, name='criar_despesa'),
    
    path('receitas/', views.listar_receitas, name='listar_receitas'),
    path('receitas/criar/', views.criar_receita, name='criar_receita'),
]
