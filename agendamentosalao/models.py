from django.db import models

# Create your models here.

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15)
    email = models.EmailField(blank=True, null=True)
    
    def __str__(self):
        return self.nome

class Profissional(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=15)
    especialidade = models.CharField(max_length=100)
   

    def __str__(self):
        return self.nome
    
class Servico(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    duracao = models.DurationField()
    preco = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.nome
    
class Agendamento(models.Model):
    STATUS = [
        ('Agendado', 'Agendado'),
        ('Concluido', 'Concluido'),
        ('Cancelado', 'Cancelado'),
    ]

    servico = models.ForeignKey(Servico, on_delete=models.CASCADE)
    profissional = models.ForeignKey(Profissional, on_delete=models.CASCADE)
    cliente_nome = models.CharField(max_length=100)
    cliente_telefone = models.CharField(max_length=15)
    data = models.DateField()
    horario = models.TimeField()

    status =  models.CharField(max_length=10, choices=STATUS, default='Agendado')

    class Meta:
        unique_together = ['profissional', 'data', 'horario']  # evita conflitos de horário
    
    def __str__(self):
        return f"{self.cliente_nome} - {self.servico.nome} com {self.profissional.nome} em {self.data_hora}"

class Relatorio(models.Model):
    titulo = models.CharField(max_length=100)
    conteudo = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo