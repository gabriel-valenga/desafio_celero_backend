import json

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from .csv_importer import importar_dados_padrao
from .models import Noc, Atleta, Time
from .serializers import NocSerializer, AtletaSerializer, TimeSerializer


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


class TimeAPIView(generics.RetrieveAPIView):
    queryset = Time.objects.all()
    serializer_class = TimeSerializer