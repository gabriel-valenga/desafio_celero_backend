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


def importar_athlete_events():
    atletas_busca = set()
    times_busca = set()
    olimpiadas_busca = set()

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
    Time.objects.bulk_create(times)
    Olimpiada.objects.bulk_create(olimpiadas)
    gravar_competicoes()
    gravar_competicoesatletas()


def limpar_listas():
    erros_importacao.clear()
    nocs.clear()
    atletas.clear()
    times.clear()
    olimpiadas.clear()
    competicoes.clear()
    competicoes_atletas.clear


def gravar_competicoes():
    competicoes_busca = set()

    with open('static/athlete_events.csv', 'r') as arquivo_csv:
        linhas = csv.DictReader(arquivo_csv)

        for linha in linhas:
            competicao_chave_composta = linha['Games'] + ' - ' + \
                                        linha['Sport'] + ' - ' + linha['Event']

            olimpiada = Olimpiada.objects.get(nome=linha['Games'])

            if competicao_chave_composta not in competicoes_busca:
                competicao = Competicao(olimpiada=olimpiada,
                                        esporte=linha['Sport'],
                                        modalidade=linha['Event'])
                competicoes.append(competicao)
                competicoes_busca.add(competicao_chave_composta)

    Competicao.objects.bulk_create(competicoes)


def gravar_competicoesatletas():
    competicoes_atletas_busca = set()
    competicao_atleta_id = 1

    with open('static/athlete_events.csv', 'r') as arquivo_csv:
        linhas = csv.DictReader(arquivo_csv)

        for linha in linhas:

            if competicao_atleta_id not in competicoes_atletas_busca:

                olimpiada = Olimpiada.objects.get(nome=linha['Games'])
                competicao = Competicao.objects.get(olimpiada=olimpiada,
                                                    esporte=linha['Sport'],
                                                    modalidade=linha['Event'])
                atleta = Atleta.objects.get(id=linha['ID'])
                time = Time.objects.get(nome=linha['Team'])

                idade = linha['Age']

                if not idade.isdigit():
                    idade = None

                altura = linha['Height']

                if not altura.isdigit():
                    altura = None

                peso = linha['Weight']

                if not peso.isdigit():
                    peso = None

                competicao_atleta = CompeticaoAtleta(competicao=competicao,
                                                     atleta=atleta,
                                                     idade_atleta=idade,
                                                     altura_atleta=altura,
                                                     peso_atleta=peso,
                                                     time=time,
                                                     medalha=linha['Medal'])
                competicoes_atletas.append(competicao_atleta)
                competicoes_atletas_busca.add(competicao_atleta_id)

            competicao_atleta_id += 1

    CompeticaoAtleta.objects.bulk_create(competicoes_atletas)


def importar_dados_padrao():
    limpar_listas()

    try:
        Noc.objects.all().delete()
    except RestrictedError:
        raise Exception('Erro de restricao ao apagar os dados da tabela noc. '
                        'Os dados da tabela time devem ser excluidos antes.')

    importar_noc_regions()
    Noc.objects.bulk_create(nocs)

    Atleta.objects.all().delete()
    Time.objects.all().delete()

    try:
        Olimpiada.objects.all().delete()
    except RestrictedError:
        raise Exception('Erro de restricao ao apagar os dados da tabela olimpiada. '
                        'Os dados da tabela competicao devem ser excluidos antes.')

    Competicao.objects.all().delete()
    CompeticaoAtleta.objects.all().delete()

    importar_athlete_events()

    if len(erros_importacao) == 0:
        limpar_dados_db()
        criar_dados_db()

    return erros_importacao
