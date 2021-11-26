from django.urls import path

from .views import (
    ImportarDadosCsvPadraoAPIView, NocsAPIView, NocAPIView, AtletasAPIView,
    AtletaAPIView, TimesAPIView, TimeAPIView, OlimpiadasAPIView, OlimpiadaAPIView,
    CompeticoesAPIView, CompeticaoAPIView, CompeticoesAtletasAPIView, CompeticaoAtletaAPIView
)

urlpatterns = [
    path('importarpadrao/', ImportarDadosCsvPadraoAPIView.as_view(), name='importarpadrao'),
    path('nocs/', NocsAPIView.as_view(), name='nocs'),
    path('nocs/<int:pk>/', NocAPIView.as_view(), name='noc'),
    path('atletas/', AtletasAPIView.as_view(), name='atletas'),
    path('atletas/<int:pk>/', AtletaAPIView.as_view(), name='atleta'),
    path('times/', TimesAPIView.as_view(), name='times'),
    path('times/<int:pk>/', TimeAPIView.as_view(), name='time'),
    path('olimpiadas/', OlimpiadasAPIView.as_view(), name='olimpiadas'),
    path('olimpiadas/<int:pk>/', OlimpiadaAPIView.as_view(), name='olimpiada'),
    path('competicoes/', CompeticoesAPIView.as_view(), name='competicoes'),
    path('competicoes/<int:pk>/', CompeticaoAPIView.as_view(), name='competicao'),
    path('competicoes_atletas/', CompeticoesAtletasAPIView.as_view(), name='competicoes_atletas'),
    path('competicoes_atletas/<int:pk>/', CompeticaoAtletaAPIView.as_view(), name='competicao_atleta'),
    path('competicoes_atletas/atletas/<int:atleta_pk>/', CompeticoesAtletasAPIView.as_view(),
         name='competicoes_atletas_por_atleta'),
    path('competicoes_atletas/olimpiadas/<str:olimpiada_pk>/', CompeticoesAtletasAPIView.as_view(),
         name='competicoes_atletas_por_olimpiada'),
    path('competicoes_atletas/competicoes/<int:competicao_pk>/', CompeticoesAtletasAPIView.as_view(),
         name='competicoes_atletas_por_competicao'),
    path('competicoes_atletas/times/<int:time_pk>/', CompeticoesAtletasAPIView.as_view(),
         name='competicoes_atletas_por_time')
]
