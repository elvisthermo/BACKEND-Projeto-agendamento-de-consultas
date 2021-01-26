from django.db import models

# Create your models here.

class Cliente(models.Model):

    nome = models.CharField(max_length=255)
    endereco = models.CharField(max_length=255)
    cpf = models.CharField(primary_key=True, max_length=11) #11
    data_nascimento = models.CharField(max_length=10, default="")
    grupo_de_risco = models.BooleanField(max_length=255,default=False)
    telefone = models.CharField(max_length=255,default="91999999999")
    url_img = models.CharField(max_length=255, default="img.jpg")
    email = models.CharField(max_length=255, default="contato@email.com")
    senha = models.CharField(max_length=20, default="PADRAO")

    def __str__(self):
        return self.nome  

class Especialidade(models.Model):
    tipo = models.CharField(max_length=255, default="")
    
    def __str__(self):
        return self.tipo

class Medico(models.Model):

    nome = models.CharField(max_length=255)
    crm = models.CharField(max_length=13, primary_key=True)
    cpf = models.CharField(max_length=11) #11
    data_nascimento = models.CharField(max_length=10,default="")
    especialidade = models.OneToOneField(Especialidade, on_delete=models.CASCADE,default=None)
    telefone = models.CharField(max_length=255,default="91999999999")
    url_img = models.CharField(max_length=255, default="img.jpg")
    email = models.CharField(max_length=255, default="contato@email.com")
    senha = models.CharField(max_length=20, default="PADRAO")
    def __str__(self):
        return self.nome

class Clinica(models.Model):
    razao_social = models.CharField(max_length=255)
    nome_fantasia = models.CharField(max_length=255)
    cnpj = models.CharField(primary_key=True, max_length=14) #14
    endereco = models.CharField(max_length=255)
    telefone = models.CharField(max_length=255,default="91999999999")
    url_img = models.CharField(max_length=255, default="img.jpg")
    email = models.CharField(max_length=255, default="contato@email.com")
    senha = models.CharField(max_length=20, default="PADRAO")

    def __str__(self):
        return self.nome_fantasia

class Consulta(models.Model):
    MODALIDADE = [
        ("PRESENCIAL","Presencial"),
        ("ONLINE","Online"),
        ("DOMICILIO","Domicilio")
    ]
    numero_consulta = models.CharField(max_length=255)
    cliente_cpf = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    medico_crm = models.ForeignKey(Medico, on_delete=models.CASCADE)
    clinica_cnpj = models.ForeignKey(Clinica, on_delete=models.CASCADE)
    data = models.CharField(max_length=10,default="") #01/11/2021
    hora = models.CharField(max_length=5, default="") #14:30
    tipo_consulta = models.CharField(max_length=20, choices=MODALIDADE,default="PRESENCIAL")
    
    def __str__(self):
        return self.cliente_cpf

