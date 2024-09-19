from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pacientes/', include('pacientes.urls')),
    path('profissionais/', include('profissionais.urls')),
    path('agendamentos/', include('agendamentos.urls')),
    path('atendimento/', include('atendimento.urls')),
    path('financeiro/', include('financeiro.urls')),
]
