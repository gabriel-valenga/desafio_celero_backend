from django.urls import path

from .views import ImportarDadosCsvPadraoAPIView

urlpatterns = [
    path('importarpadrao/', ImportarDadosCsvPadraoAPIView.as_view(), name='importarpadrao')
]
