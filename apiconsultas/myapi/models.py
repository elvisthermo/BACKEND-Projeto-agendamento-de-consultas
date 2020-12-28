from django.db import models

# Create your models here.

class Cliente(models.Model):

    nome = models.CharField(max_length=255)
    idade = models.IntegerField()
    endereco = models.CharField(max_length=255)
    cpf = models.IntegerField(primary_key=True) #11
    grupo_de_risco = 
    def __str__(self):
        return self.nome  

class Medico(models.Model):

    nome = models.CharField(max_length=255)
    crm = models.CharField(max_length=13, primary_key=True)
    cpf = models.IntegerField() #11
    are_atuacao = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

class Clinica(models.Model):
    razao_social = models.CharField(max_length=255)
    nome_fantasia = models.CharField(max_length=255)
    cnpj = models.IntegerField( primary_key=True) #14
    endereco = models.CharField(max_length=255)

    def __str__(self):
        return self.nome_fantasia

class Consulta(models.Model):
    numero_consulta = models.
    clinte_cpf = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    medico_crm = models.ForeignKey(Medico, on_delete=models.CASCADE)
    clinica_cnpj = models.ForeignKey(Clinica, on_delete=models.CASCADE)
    data_hora = models.DateTimeField()
    tipo_consulta = models.CharField(max_length=255)
    grupo_de_risco = models.CharField(max_length=3)

