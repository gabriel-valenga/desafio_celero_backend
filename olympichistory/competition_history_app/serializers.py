from rest_framework import serializers
from .models import Noc, Atleta, Time


class NocSerializer(serializers.ModelSerializer):

    class Meta:
        model = Noc
        fields = (
            'id',
            'sigla',
            'regiao',
            'observacoes'
        )


class AtletaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Atleta
        fields = (
            'id',
            'nome',
            'sexo'
        )


class TimeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Time
        fields = (
            'id',
            'nome',
            'noc'
        )
