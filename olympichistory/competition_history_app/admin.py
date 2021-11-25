from django.contrib import admin
from .models import (
    Noc,
    Atleta,
    Time,
    Olimpiada,
    Competicao,
    CompeticaoAtleta
)


@admin.register(Noc)
class NocAdmin(admin.ModelAdmin):
    list_display = ('sigla', 'regiao', 'criacao_registro', 'atualizacao_registro')


@admin.register(Atleta)
class AtletaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'criacao_registro', 'atualizacao_registro')


@admin.register(Time)
class TimeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'noc', 'criacao_registro', 'atualizacao_registro')


@admin.register(Olimpiada)
class OlimpiadaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ano', 'criacao_registro', 'atualizacao_registro')


@admin.register(Competicao)
class CompeticaoAdmin(admin.ModelAdmin):
    list_display = ('id', 'olimpiada', 'esporte', 'modalidade', 'criacao_registro', 'atualizacao_registro')


@admin.register(CompeticaoAtleta)
class CompeticaoAtletaAdmin(admin.ModelAdmin):
    list_display = ('id', 'competicao', 'atleta', 'criacao_registro', 'atualizacao_registro')
