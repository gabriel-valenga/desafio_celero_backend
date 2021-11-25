import json

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .csv_importer import importar_dados_padrao
from .models import Noc
from .serializers import NocSerializer


class ImportarDadosCsvPadraoAPIView(APIView):
    """
    Importa os Nocs do arquivo CSV
    """

    def post(self, request):
        erros = importar_dados_padrao()
        if len(erros) > 0:
            return Response(data=json.dumps({"erros_importacao": erros}), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(status=status.HTTP_201_CREATED)
