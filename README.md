# desafio_celero_backend
Api Rest para servir os dados do dataset “120 years of Olympic history"


Imports necessários:

asgiref==3.4.1
Django==3.2.9
django-filter==21.1
djangorestframework==3.12.4
importlib-metadata==4.8.2
Markdown==3.3.6
pytz==2021.3
sqlparse==0.4.2
zipp==3.6.0



                          ROTAS:

POST:

- Importar todos os dados padrão: 
 
  '/historyapi/importarpadrao/'

(O procedimento acima leva aproximadamente 27 minutos)


- Criar Noc: 

  '/historyapi/nocs/


- Criar Atleta: 

  '/historyapi/atletas/


- Criar Time: 

  '/historyapi/times/


- Criar Olimpiada: 

  '/historyapi/olimpiadas/


- Criar Competicao: 

  '/historyapi/competicoes/


- Criar CompeticaoAtleta: 

  '/historyapi/competicoesatletas/



GET:

- Buscar todos os Nocs: 

  '/historyapi/nocs/


- Buscar um Noc (pk é o id): 

  '/historyapi/nocs/<int:pk>/


- Buscar todos os Atletas: 

  '/historyapi/atletas/


- Buscar um Atleta (pk é o id): 

  '/historyapi/atletas/<int:pk>/
  

- Buscar todos os Times: 

  '/historyapi/times/


- Buscar um Time (pk é o id): 

  '/historyapi/times/<int:pk>/


- Buscar todas as Olimpiadas: 

  '/historyapi/olimpiadas/


- Buscar uma Olimpiada (pk é o nome): 

  '/historyapi/olimpiadas/<str:pk>/


- Buscar todas as Competicoes: 

  '/historyapi/competicoes/


- Buscar uma Competicao (pk é o id): 

  '/historyapi/competicoes/<int:pk>/


- Buscar todas as CompeticoesAtletas: 

  '/historyapi/competicoesatletas/


- Buscar uma CompeticaoAtleta: 

  '/historyapi/competicoesatletas/<int:pk>/


- Buscar CompeticoesAtletas por Atleta (atleta_pk é o id do Atleta): 

  '/historyapi/competicoesatletas/atletas/<int:atleta_pk>/


- Buscar CompeticoesAtletas por Olimpiada (olimpiada_pk é o nome da Olimpiada): 

  '/historyapi/competicoesatletas/olimpiadas/<str:olimpiada_pk>/


- Buscar CompeticoesAtletas por Competicao (competicao_pk é o id da Competicao): 

  '/historyapi/competicoesatletas/competicoes/<int:competicao_pk>/


- Buscar CompeticoesAtletas por Time (time_pk é o id do Time): 

  '/historyapi/competicoesatletas/times/<int:time_pk>/



PUT:

- Atualizar um Noc (pk é o id): 

  '/historyapi/nocs/<int:pk>/


- Atualizar um Atleta (pk é o id): 

  '/historyapi/atletas/<int:pk>/


- Atualizar um Time (pk é o id): 

  '/historyapi/times/<int:pk>/


- Atualizar uma Olimpiada (pk é o nome): 

  '/historyapi/olimpiadas/<str:pk>/


- Atualizar uma Competicao (pk é o id): 

  '/historyapi/competicoes/<int:pk>/


- Atualizar uma CompeticaoAtleta: 

  '/historyapi/competicoesatletas/<int:pk>/


DELETE:

- Apagar um Noc (pk é o id): 

  '/historyapi/nocs/<int:pk>/


- Apagar um Atleta (pk é o id): 

  '/historyapi/atletas/<int:pk>/


- Apagar um Time (pk é o id): 

  '/historyapi/times/<int:pk>/


- Apagar uma Olimpiada (pk é o nome): 

  '/historyapi/olimpiadas/<str:pk>/


- Apagar uma Competicao (pk é o id): 

  '/historyapi/competicoes/<int:pk>/


- Apagar uma CompeticaoAtleta: 

  '/historyapi/competicoesatletas/<int:pk>/