from rest_framework import serializers
from .models import Noc


class NocSerializer(serializers.ModelSerializer):

    class Meta:
        model = Noc
        fields = {
            'id',
            'sigla',
            'regiao',
            'observacoes'
        }