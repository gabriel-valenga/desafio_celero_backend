import json

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from .csv_importer import importar_dados_padrao
from .models import Noc, Atleta, Time, Olimpiada, Competicao, CompeticaoAtleta
from .serializers import (
    NocSerializer, AtletaSerializer, TimeSerializer, OlimpiadaSerializer,
    CompeticaoSerializer, CompeticaoAtletaSerializer
)


class ImportarDadosCsvPadraoAPIView(APIView):
    """
    Importa os Nocs do arquivo CSV
    """

    def post(self, request):
        erros = importar_dados_padrao()
        if len(erros) > 0:
            return Response(data=json.dumps({"erros_importacao": erros}), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(status=status.HTTP_201_CREATED)


class NocsAPIView(generics.ListCreateAPIView):
    queryset = Noc.objects.all()
    serializer_class = NocSerializer


class NocAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Noc.objects.all()
    serializer_class = NocSerializer


class AtletasAPIView(generics.ListCreateAPIView):
    queryset = Atleta.objects.all()
    serializer_class = AtletaSerializer


class AtletaAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Atleta.objects.all()
    serializer_class = AtletaSerializer


class TimesAPIView(generics.ListCreateAPIView):
    queryset = Time.objects.all()
    serializer_class = TimeSerializer


class TimeAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Time.objects.all()
    serializer_class = TimeSerializer


class OlimpiadasAPIView(generics.ListCreateAPIView):
    queryset = Olimpiada.objects.all()
    serializer_class = OlimpiadaSerializer


class OlimpiadaAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Olimpiada.objects.all()
    serializer_class = OlimpiadaSerializer


class CompeticoesAPIView(generics.ListCreateAPIView):
    queryset = Competicao.objects.all()
    serializer_class = CompeticaoSerializer


class CompeticaoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Competicao.objects.all()
    serializer_class = CompeticaoSerializer


class CompeticoesAtletasAPIView(generics.ListCreateAPIView):
    queryset = CompeticaoAtleta.objects.all()
    serializer_class = CompeticaoAtletaSerializer

    def get_queryset(self):
        busca_por_atleta = self.kwargs.get('atleta_pk')
        busca_por_olimpiada = self.kwargs.get('olimpiada_pk')
        busca_por_competicao = self.kwargs.get('competicao_pk')
        busca_por_time = self.kwargs.get('time_pk')
        if busca_por_atleta:
            return self.queryset.filter(atleta=busca_por_atleta)
        if busca_por_olimpiada:
            return self.queryset.filter(olimpiada=busca_por_olimpiada)
        if busca_por_competicao:
            return self.queryset.filter(competicao=busca_por_competicao)
        if busca_por_time:
            return self.queryset.filter(time=busca_por_time)

        return self.queryset.all()


class CompeticaoAtletaAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CompeticaoAtleta.objects.all()
    serializer_class = CompeticaoAtletaSerializer

