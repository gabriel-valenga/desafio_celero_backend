import csv
from .models import Noc, Atleta, Time, Olimpiada, Competicao, CompeticaoAtleta
from django.db.models.deletion import RestrictedError

nocs = []
atletas = []
times = []
olimpiadas = []
competicoes = []
competicoes_atletas = []
erros_importacao = []


def importar_noc_regions():
    nocs_busca = set()
    with open('static/noc_regions.csv', 'r') as arquivo_csv:
        linhas = csv.DictReader(arquivo_csv)
        for linha in linhas:
            if linha['NOC'] not in nocs_busca:
                noc = Noc(sigla=linha['NOC'], regiao=linha['region'],
                          observacoes=linha['notes'])
                nocs.append(noc)
                nocs_busca.add(linha['NOC'])

    Noc.objects.bulk_create(nocs)


def importar_athlete_events():
    atletas_busca = set()
    times_busca = set()
    olimpiadas_busca = set()
    competicoes_busca = set()
    competicao_atleta_lista_dicts = []
    competicao_atleta_id = 1

    with open('static/athlete_events.csv', 'r') as arquivo_csv:
        linhas = csv.DictReader(arquivo_csv)
        for linha in linhas:

            if linha['ID'] not in atletas_busca:
                atleta = Atleta(id=linha['ID'], nome=linha['Name'],
                                sexo=linha['Sex'])
                atletas.append(atleta)
                atletas_busca.add(linha['ID'])

            try:
                noc = Noc.objects.get(sigla=linha['NOC'])
            except Noc.DoesNotExist as e:
                erro_nao_existe_noc = linha['NOC'] + ' nao existe na tabela noc'

                if erros_importacao.count(erro_nao_existe_noc) == 0:
                    erros_importacao.append(erro_nao_existe_noc)

            if linha['Team'] not in times_busca:
                time = Time(nome=linha['Team'], noc=noc)
                times.append(time)
                times_busca.add(linha['Team'])

            if linha['Games'] not in olimpiadas_busca:
                olimpiada = Olimpiada(nome=linha['Games'], ano=linha['Year'],
                                      estacao=linha['Season'],
                                      cidade=linha['City'])
                olimpiadas.append(olimpiada)
                olimpiadas_busca.add(linha['Games'])

            competicao_chave_composta = linha['Sport'] + ' - ' + linha['Event']

            if competicao_chave_composta not in competicoes_busca:
                competicao = Competicao(esporte=linha['Sport'],
                                        modalidade=linha['Event'])
                competicoes.append(competicao)
                competicoes_busca.add(competicao_chave_composta)

            idade = linha['Age']
            if not idade.isdigit():
                idade = None
            altura = linha['Height']
            if not altura.isdigit():
                altura = None
            peso = linha['Weight']
            if not peso.isdigit():
                peso = None

            competicao_atleta_lista_dicts.append(
                {'competicao': {'esporte': linha['Sport'],
                                'modalidade': linha['Event']},
                 'olimpiada': linha['Games'],
                 'atleta': linha['ID'],
                 'idade_atleta': idade,
                 'altura_atleta': altura,
                 'peso_atleta': peso,
                 'time': linha['Team'],
                 'medalha': linha['Medal']})

            competicao_atleta_id += 1

    Atleta.objects.bulk_create(atletas)
    Time.objects.bulk_create(times)
    Olimpiada.objects.bulk_create(olimpiadas)
    Competicao.objects.bulk_create(competicoes)

    for comp_atleta_dict in competicao_atleta_lista_dicts:

        competicao_atleta_competicao =\
            Competicao.objects.get(esporte=comp_atleta_dict.get('competicao').get('esporte'),
                                   modalidade=comp_atleta_dict.get('competicao').get('modalidade'))
        competicao_atleta_olimpiada = Olimpiada.objects.get(nome=comp_atleta_dict.get('olimpiada'))
        competicao_atleta_atleta = Atleta.objects.get(id=comp_atleta_dict.get('atleta'))
        competicao_atleta_time = Time.objects.get(nome=comp_atleta_dict.get('time'))

        competicao_atleta = CompeticaoAtleta(competicao=competicao_atleta_competicao,
                                             olimpiada=competicao_atleta_olimpiada,
                                             atleta=competicao_atleta_atleta,
                                             idade_atleta=comp_atleta_dict.get('idade_atleta'),
                                             altura_atleta=comp_atleta_dict.get('altura_atleta'),
                                             peso_atleta=comp_atleta_dict.get('peso_atleta'),
                                             time=competicao_atleta_time,
                                             medalha=comp_atleta_dict.get('medalha'))
        competicoes_atletas.append(competicao_atleta)
    CompeticaoAtleta.objects.bulk_create(competicoes_atletas)


def limpar_dados_db():

    CompeticaoAtleta.objects.all().delete()

    try:
        Competicao.objects.all().delete()
    except RestrictedError:
        raise Exception('Erro de restricao ao apagar os dados da tabela competicao. '
                        'Os dados da tabela competicao_atleta devem ser excluidos antes.')

    try:
        Olimpiada.objects.all().delete()
    except RestrictedError:
        raise Exception('Erro de restricao ao apagar os dados da tabela olimpiada. '
                        'Os dados da tabela competicao devem ser excluidos antes.')

    try:
        Time.objects.all().delete()
    except RestrictedError:
        raise Exception('Erro de restricao ao apagar os dados da tabela time. '
                        'Os dados da tabela competicao_atleta devem ser excluidos antes.')
    try:
        Atleta.objects.all().delete()
    except RestrictedError:
        raise Exception('Erro de restricao ao apagar os dados da tabela atleta. '
                        'Os dados da tabela competicao_atleta devem ser excluidos antes.')

    try:
        Noc.objects.all().delete()
    except RestrictedError:
        raise Exception('Erro de restricao ao apagar os dados da tabela noc. '
                        'Os dados da tabela time devem ser excluidos antes.')


def limpar_listas():
    erros_importacao.clear()
    nocs.clear()
    atletas.clear()
    times.clear()
    olimpiadas.clear()
    competicoes.clear()
    competicoes_atletas.clear()


def importar_dados_padrao():
    limpar_listas()
    limpar_dados_db()
    importar_noc_regions()
    importar_athlete_events()

    return erros_importacao
