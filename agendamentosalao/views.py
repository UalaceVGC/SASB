from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from datetime import timedelta
from . models import *
from django.core.paginator import Paginator
from django.db.models import Q
# Página inicial
def home(request):
    clientes = Cliente.objects.all()
    profissionais = Profissional.objects.all()
    servicos = Servico.objects.all()
    agendamentos = Agendamento.objects.all().filter(status='Agendado').order_by('-data', '-horario')  # Filtra apenas agendamentos pendentes

    context = {
        'clientes': clientes,
        'profissionais': profissionais,
        'servicos': servicos,
        'agendamentos': agendamentos,
    }
    
    return render(request, 'base/base.html', context)

# Funcionalidade da equipe
def equipe(request):
    pesquisa = request.GET.get('pesquisar', '').strip()
    if pesquisa:    
        profissionais = Profissional.objects.filter(
            Q(nome__icontains=pesquisa) |
            Q(especialidade__icontains=pesquisa) |
            Q(email__icontains=pesquisa) |
            Q(telefone__icontains=pesquisa)
        )  
    else:
        # Se não houver pesquisa, retorna todos os profissionais
        profissionais = Profissional.objects.all()
    
    paginator = Paginator(profissionais, 5)  # Limitar para 5 profissionais por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'agendamentosalaoapp/recepcionista/listagem/listagem_equipe.html', 
        {
            'profissionais': page_obj.object_list,
            'page_obj': page_obj,
        }
    )
def cadastrar_profissional(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        especialidade = request.POST.get('especialidade')

        #Criando o objeto Profissional e salvando no banco de dados
        profissional = Profissional(nome=nome, email=email, telefone=telefone, especialidade=especialidade)
        profissional.save()
        messages.success(request, 'Profissional cadastrado com sucesso!')
        return redirect('equipe')

    return render(request, 'agendamentosalaoapp/recepcionista/cadastro/cadastro_funcionario.html')

def editar_profissional(request, profissional_id):
    profissional = get_object_or_404(Profissional, id=profissional_id)

    if request.method == 'POST':
        profissional.nome = request.POST.get('nome')
        profissional.email = request.POST.get('email')
        profissional.telefone = request.POST.get('telefone')
        profissional.especialidade = request.POST.get('especialidade')
        profissional.save() #Salvando as alterações no banco de dados
        messages.success(request, 'Profissional atualizado com sucesso!')
        return redirect('equipe')

    return render(request, 'agendamentosalaoapp/recepcionista/editar/edt_funcionario.html', {'profissional': profissional})

def deletar_profissional(request, profissional_id):
    profissional = get_object_or_404(Profissional, id=profissional_id)
    
    if profissional == None: # Só por formalidade, caso o profissional não exista
        messages.error(request, 'Profissional não encontrado.')
        return redirect('equipe')
    else:
        profissional.delete() # Deletando o profissional
        messages.success(request, 'Profissional deletado com sucesso!')
        return redirect('equipe')   

    


# Funcionalidade da Clientes
def clientes(request):
    pesquisa = request.GET.get('pesquisar', '').strip()
    if pesquisa:
        clientes = Cliente.objects.filter(
            Q(nome__icontains=pesquisa) |
            Q(telefone__icontains=pesquisa) |
            Q(email__icontains=pesquisa)
        )
    else:
        # Se não houver pesquisa, retorna todos os clientes
        clientes = Cliente.objects.all()

    # Paginação
    paginator = Paginator(clientes, 5)  # Limitar para 5 clientes por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'agendamentosalaoapp/recepcionista/listagem/listagem_clientes.html', 
        {
          'clientes': page_obj.object_list,
          'page_obj': page_obj,
        } 
    )

def cadastrar_cliente(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        telefone = request.POST.get('telefone')
        email = request.POST.get('email')

        #Criando o objeto Cliente e salvando no banco de dados
        cliente = Cliente(nome=nome, telefone=telefone, email=email)
        cliente.save()
        messages.success(request, 'Cliente cadastrado com sucesso!')
        return redirect('clientes')

    return render(request, 'agendamentosalaoapp/recepcionista/cadastro/cadastro_cliente.html')

def editar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)

    if request.method == 'POST':
        cliente.nome = request.POST.get('nome')
        cliente.email = request.POST.get('email')
        cliente.telefone = request.POST.get('telefone')
        cliente.save() #Salvando as alterações no banco de dados
        messages.success(request, 'Cliente atualizado com sucesso!')
        return redirect('clientes')

    return render(request, 'agendamentosalaoapp/recepcionista/editar/edt_cliente.html', {'cliente': cliente})

def deletar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    
    if cliente == None: # Só por formalidade, caso o cliente não exista
        messages.error(request, 'Cliente não encontrado.')
        return redirect('clientes')
    else:
        cliente.delete() # Deletando o cliente
        messages.success(request, 'Cliente deletado com sucesso!')
        return redirect('clientes')
    
    

# Funcionalidade da Serviços
def servicos(request):
    pesquisa = request.GET.get('pesquisar', '').strip()
    if pesquisa:
        servicos = Servico.objects.filter(
            Q(nome__icontains=pesquisa) |
            Q(descricao__icontains=pesquisa) |
            Q(preco__icontains=pesquisa)
        )
    else:
        # Se não houver pesquisa, retorna todos os serviços
        servicos = Servico.objects.all()
    paginator = Paginator(servicos, 5)  # Limitar para 5 serviços por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'agendamentosalaoapp/recepcionista/listagem/listagem_servicos.html', 
        {
            'servicos': page_obj.object_list,
            'page_obj': page_obj,
        } 
    )

def cadastrar_servico(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')
        duracao_str = request.POST.get('duracao')  # Recebe como string
        preco = request.POST.get('preco')

        # Converte "HH:MM:SS" para timedelta
        h, m, s = map(int, duracao_str.split(':'))
        duracao = timedelta(hours=h, minutes=m, seconds=s)

        servico = Servico(nome=nome, descricao=descricao, duracao=duracao, preco=preco)
        servico.save()
        messages.success(request, 'Serviço cadastrado com sucesso!')
        return redirect('servicos')

    return render(request, 'agendamentosalaoapp/recepcionista/cadastro/cadastro_servicos.html')

def editar_servico(request, servico_id):
    servico = get_object_or_404(Servico, id=servico_id)

    if request.method == 'POST':
        
        servico.nome = request.POST.get('nome')
        servico.descricao = request.POST.get('descricao')
        duracao_str = request.POST.get('duracao')

        # Converte "HH:MM:SS" para timedelta
        h, m, s = map(int, duracao_str.split(':'))
        duracao_str = timedelta(hours=h, minutes=m, seconds=s)

        servico.duracao = duracao_str
        servico.preco = request.POST.get('preco')

        servico.save() #Salvando as alterações no banco de dados
        messages.success(request, 'Serviço atualizado com sucesso!')
        return redirect('servicos')

    return render(request, 'agendamentosalaoapp/recepcionista/editar/edt_servicos.html', {'servico': servico})

def deletar_servico(request, servico_id):
    servico = get_object_or_404(Servico, id=servico_id)
    
    if servico == None:
        messages.error(request, 'Serviço não encontrado.')
        return redirect('servicos')
    else:
        servico.delete() # Deletando o serviço
        messages.success(request, 'Serviço deletado com sucesso!')  
        return redirect('servicos')


# Funcionalidade da Agendamentos
def agendamentos(request):
    pesquisa = request.GET.get('pesquisar', '').strip()
    data = request.GET.get('data', '').strip()
    agendamentos_list = Agendamento.objects.all()

    if data:
        agendamentos_list = agendamentos_list.filter(data__icontains=data)

    if pesquisa:
        agendamentos_list = agendamentos_list.filter(
            Q(cliente_nome__icontains=pesquisa ) |
            Q(profissional__nome__icontains=pesquisa) |
            Q(servico__nome__icontains=pesquisa) |
            Q(data__icontains=pesquisa) |
            Q(horario__icontains=pesquisa) |
            Q(cliente_telefone__icontains=pesquisa) |
            Q(status__icontains=pesquisa)
        )

    agendamentos_list = agendamentos_list.order_by('-data', '-horario')
    
    paginator = Paginator(agendamentos_list, 5)  # Limitar para 5 agendamentos por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'agendamentosalaoapp/recepcionista/agendamento/horarios_marcados.html', 
        {
            'agendamentos': page_obj.object_list,
            'page_obj': page_obj,
            'pesquisa': pesquisa,
            'data': data 
        }
    )
def marcar_horario(request):
    
    servicos = Servico.objects.all()
    profissionais = Profissional.objects.all()
    clientes = Cliente.objects.all()

    if request.method == 'POST':
        servico_id = request.POST.get('servico')
        profissional_id = request.POST.get('profissional')
        cliente_id = request.POST.get('cliente')
        data = request.POST.get('data')
        horario = request.POST.get('horario')

        servico = get_object_or_404(Servico, id=servico_id)
        profissional = get_object_or_404(Profissional, id=profissional_id)
        cliente = get_object_or_404(Cliente, id=cliente_id)

        agendamento = Agendamento(
            servico=servico, 
            profissional=profissional, 
            cliente_nome=cliente.nome, 
            cliente_telefone=cliente.telefone, 
            data=data, 
            horario=horario
        )
        agendamento.save()
        messages.success(request, 'Horário marcado com sucesso!')
        return redirect('agendamentos')


    return render(request, 'agendamentosalaoapp/recepcionista/agendamento/marcarhorario.html', 
                  {'servicos': servicos, 'profissionais': profissionais, 'clientes': clientes})

def editar_agendamento(request, agendamento_id):
    agendamento = get_object_or_404(Agendamento, id=agendamento_id)
    servicos = Servico.objects.all()
    profissionais = Profissional.objects.all()
    clientes = Cliente.objects.all()

    if request.method == 'POST':
        servico_id = request.POST.get('servico')
        profissional_id = request.POST.get('profissional')
        cliente_id = request.POST.get('cliente')
        data = request.POST.get('data')
        horario = request.POST.get('horario')

        servico = get_object_or_404(Servico, id=servico_id)
        profissional = get_object_or_404(Profissional, id=profissional_id)
        cliente = get_object_or_404(Cliente, id=cliente_id)

        agendamento.servico = servico
        agendamento.profissional = profissional
        agendamento.cliente_nome = cliente.nome
        agendamento.cliente_telefone = cliente.telefone
        agendamento.data = data
        agendamento.horario = horario
        agendamento.save() #Salvando as alterações no banco de dados
        messages.success(request, 'Agendamento atualizado com sucesso!')
        return redirect('agendamentos')

    return render(request, 'agendamentosalaoapp/recepcionista/agendamento/edt_agendamento.html', 
                  {'agendamento': agendamento, 'servicos': servicos, 'profissionais': profissionais, 'clientes': clientes})

def deletar_agendamento(request, agendamento_id):
    agendamento = get_object_or_404(Agendamento, id=agendamento_id)
    
    if agendamento == None(): # Só por formalidade, caso o agendamento não exista
        messages.error(request, 'Agendamento não encontrado.')
        return redirect('agendamentos')
    else:
        agendamento.delete() # Deletando o agendamento
        messages.success(request, 'Agendamento deletado com sucesso!')
        return redirect('agendamentos') 
    
def modificar_status(request, agendamento_id):
    agendamento = get_object_or_404(Agendamento, id=agendamento_id)

    if request.method == 'POST':
        novo_status = request.POST.get('status')
        agendamento.status = novo_status
        agendamento.save()  # Salva o novo status no banco de dados
        messages.success(request, 'Status do agendamento atualizado com sucesso!')
        return redirect('agendamentos')

    return render(request, 'agendamentosalaoapp/recepcionista/agendamento/modificar_status.html', {'agendamento': agendamento})

# Funcionalidade do Relatório

def relatorio_servicos(request):

    total_concluidos = None
    servicos_concluidos = []

    data_inicio = request.GET.get('data_inicio')
    data_fim = request.GET.get('data_fim')

    if data_inicio and data_fim:
        
        servicos_concluidos = Agendamento.objects.filter(
            status='Concluido',

            data__range=[
                data_inicio, data_fim
            ]
        )

        total_concluidos = servicos_concluidos.count()

    return render(request, 'agendamentosalaoapp/administrador/relatorio.html', 
        {
            'total_concluidos': total_concluidos,
            'servicos_concluidos': servicos_concluidos
        }
    )

