from rest_framework import serializers
from .models import Noc, Atleta, Time, Olimpiada, Competicao, CompeticaoAtleta


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


class OlimpiadaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Olimpiada
        fields = (
            'nome',
            'ano',
            'estacao',
            'cidade'
        )


class CompeticaoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Competicao
        fields = (
            'esporte',
            'modalidade'
        )


class CompeticaoAtletaSerializer(serializers.ModelSerializer):

    class Meta:
        model = CompeticaoAtleta
        fields = (
            'competicao',
            'olimpiada',
            'atleta',
            'idade_atleta',
            'altura_atleta',
            'peso_atleta',
            'time',
            'medalha'
        )