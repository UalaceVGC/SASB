from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),

    # Funcionalidade do equipe
    path('equipe/', views.equipe, name='equipe'),
    path('equipe/cadastrar_profissional/', views.cadastrar_profissional, name='cadastrar_profissional'),
    path('equipe/editar_profissional/<int:profissional_id>/', views.editar_profissional, name='editar_profissional'),
    path('equipe/deletar_profissional/<int:profissional_id>/', views.deletar_profissional, name='deletar_profissional'),

    # Funcionalidade do Clientes
    path('clientes/', views.clientes, name='clientes'),
    path('clientes/cadastrar_cliente/', views.cadastrar_cliente, name='cadastrar_cliente'),
    path('clientes/editar_cliente/<int:cliente_id>/', views.editar_cliente, name='editar_cliente'),
    path('clientes/deletar_cliente/<int:cliente_id>/', views.deletar_cliente, name='deletar_cliente'),

    # Funcionalidade do Serviços
    path('servicos/', views.servicos, name='servicos'),
    path('servicos/cadastrar_servico/', views.cadastrar_servico, name='cadastrar_servico'),
    path('servicos/editar_servico/<int:servico_id>/', views.editar_servico, name='editar_servico'),
    path('servicos/deletar_servico/<int:servico_id>/', views.deletar_servico, name='deletar_servico'),

    # Funcionalidade do agendamento
    path('agendamentos/', views.agendamentos, name='agendamentos'),
    path('agendamentos/marcar_horario/', views.marcar_horario, name='marcar_horario'),
    path('agendamentos/editar_agendamento/<int:agendamento_id>/', views.editar_agendamento, name='editar_agendamento'),
    path('agendamentos/deletar_agendamento/<int:agendamento_id>/', views.deletar_agendamento, name='deletar_agendamento'),  
    path('agendamentos/modificar_status/<int:agendamento_id>/', views.modificar_status, name='modificar_status'),
    
    #Funcionalidade do Relatório
    path('relatorio/', views.relatorio_servicos, name='relatorio'),

]