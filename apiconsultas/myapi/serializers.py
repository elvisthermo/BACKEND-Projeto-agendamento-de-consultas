from rest_framework import serializers
from myapi.models import Cliente, Clinica,  Medico

class ClienteSerializer(serializers.ModelSerializer):

    class Meta:

        model = Cliente
        fields = '__all__'
class MedicoSerializer(serializers.ModelSerializer):

    class Meta:

        model = Medico
        fields = '__all__'

class ClinicaSerializer(serializers.ModelSerializer):
    
    class Meta:

        model = Clinica
        fields = '__all__'