from rest_framework import serializers
from .models import Customer


class ClientesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Clientes
        fields = ('pk', 'first_name', 'last_name', 'email', 'phone', 'address', 'description')

        