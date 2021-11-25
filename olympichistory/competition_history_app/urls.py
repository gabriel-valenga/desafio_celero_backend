from django.urls import path

from .views import (
    ImportarDadosCsvPadraoAPIView, NocsAPIView, NocAPIView, AtletasAPIView,
    AtletaAPIView, TimesAPIView, TimeAPIView
)

urlpatterns = [
    path('importarpadrao/', ImportarDadosCsvPadraoAPIView.as_view(), name='importarpadrao'),
    path('nocs/', NocsAPIView.as_view(), name='nocs'),
    path('nocs/<int:pk>/', NocAPIView.as_view(), name='noc'),
    path('atletas/', AtletasAPIView.as_view(), name='atletas'),
    path('atletas/<int:pk>/', AtletaAPIView.as_view(), name='atleta'),
    path('times/', TimesAPIView.as_view(), name='times'),
    path('times/<int:pk>/', TimeAPIView.as_view(), name='time')

]
