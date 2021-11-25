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
            noc = Noc(sigla=linha['NOC'], regiao=linha['region'],
                      observacoes=linha['notes'])
            if noc.sigla not in nocs_busca:
                nocs.append(noc)
                nocs_busca.add(noc.sigla)


def importar_athlete_events():
    atletas_busca = set()
    times_busca = set()
    olimpiadas_busca = set()
    competicoes_busca = set()
    competicoes_atletas_busca = set()
    competicao_atleta_id = 1

    with open('static/athlete_events.csv', 'r') as arquivo_csv:
        linhas = csv.DictReader(arquivo_csv)
        for linha in linhas:

            atleta = Atleta(id=linha['ID'], nome=linha['Name'],
                            sexo=linha['Sex'])

            try:
                noc = Noc.objects.get(sigla=linha['NOC'])
            except Noc.DoesNotExist as e:
                erro_nao_existe_noc = linha['NOC'] + ' nao existe na tabela noc'

                if erros_importacao.count(erro_nao_existe_noc) == 0:
                    erros_importacao.append(erro_nao_existe_noc)

            time = Time(nome=linha['Team'], noc=noc)

            olimpiada = Olimpiada(nome=linha['Games'], ano=linha['Year'],
                                  estacao=linha['Season'],
                                  cidade=linha['City'])

            competicao = Competicao(olimpiada=olimpiada,
                                    esporte=linha['Sport'],
                                    modalidade=linha['Event'])

            competicao_chave_composta = linha['Games'] + ' - ' + \
                linha['Sport'] + ' - ' + linha['Event']

            competicao_atleta = CompeticaoAtleta(competicao=competicao,
                                                 atleta=atleta,
                                                 idade_atleta=linha['Age'],
                                                 altura_atleta=linha['Height'],
                                                 peso_atleta=linha['Weight'],
                                                 medalha=linha['Medal'])

            if atleta.id not in atletas_busca:
                atletas.append(atleta)
                atletas_busca.add(atleta.id)
                print(atleta.id)

            if time.nome not in times_busca:
                times.append(time)
                times_busca.add(time.nome)

            if olimpiada.nome not in olimpiadas_busca:
                olimpiadas.append(olimpiada)
                olimpiadas_busca.add(olimpiada.nome)

            if competicao_chave_composta not in competicoes_busca:
                competicoes.append(competicao)
                competicoes_busca.add(competicao_chave_composta)

            if competicao_atleta_id not in competicoes_atletas_busca:
                competicoes_atletas.append(competicao_atleta)
                competicoes_atletas_busca.add(competicao_atleta_id)

            competicao_atleta_id += 1


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


def criar_dados_db():
    Atleta.objects.bulk_create(atletas)
    Olimpiada.objects.bulk_create(olimpiadas)
    Time.objects.bulk_create(times)
    Competicao.objects.bulk_create(competicoes)
    CompeticaoAtleta.objects.bulk_create(competicoes_atletas)


def limpar_listas():
    erros_importacao.clear()
    nocs.clear()
    atletas.clear()
    olimpiadas.clear()
    times.clear()
    competicoes.clear()
    competicoes_atletas.clear


def importar_dados_padrao():
    limpar_listas()
    importar_noc_regions()

    try:
        Noc.objects.all().delete()
    except RestrictedError:
        raise Exception('Erro de restricao ao apagar os dados da tabela noc. '
                        'Os dados da tabela time devem ser excluidos antes.')

    Noc.objects.bulk_create(nocs)
    importar_athlete_events()

    if len(erros_importacao) == 0:
        limpar_dados_db()
        criar_dados_db()

    return erros_importacao


