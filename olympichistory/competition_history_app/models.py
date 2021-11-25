from django.db import models

SEXO = (
    ('F', 'Feminino'),
    ('M', 'Masculino'),
    ('O', 'Outro')
)

ESTACOES_ANO_OLIMPICAS = (
    ('Summer', 'Verão'),
    ('Winter', 'Inverno')
)
MEDALHA = (
    ('Golden', 'Ouro'),
    ('Silver', 'Prata'),
    ('Bronze', 'Bronze'),
    ('NA', 'Sem medalha')
)


class Base(models.Model):
    criacao_registro = models.DateTimeField(auto_now_add=True),
    atualizacao_registro = models.DateTimeField(auto_now=True),

    class Meta:
        abstract = True


class Noc(Base):
    sigla = models.CharField(max_length=3, unique=True, blank=False)
    regiao = models.CharField(max_length=50, blank=False)
    observacoes = models.CharField(max_length=100, blank=True)

    class Meta:
        verbose_name = 'Noc'
        verbose_name_plural = 'Nocs'

    def __str__(self):
        return self.sigla


class Atleta(Base):
    nome = models.CharField(max_length=100, blank=False)
    sexo = models.CharField(max_length=1, choices=SEXO, blank=False)

    class Meta:
        verbose_name = 'Atleta'
        verbose_name_plural = 'Atletas'


class Time(Base):
    nome = models.CharField(max_length=70, unique=True, blank=False)
    noc = models.ForeignKey(Noc, to_field='sigla', max_length=3, null=False, on_delete=models.RESTRICT)

    class Meta:
        verbose_name = 'Time'
        verbose_name_plural = 'Times'


class Olimpiada(Base):
    nome = models.CharField(max_length=100, unique=True, blank=False)
    ano = models.IntegerField(null=False)
    estacao = models.CharField(max_length=6, choices=ESTACOES_ANO_OLIMPICAS, blank=False)
    cidade = models.CharField(max_length=70, blank=False)

    class Meta:
        verbose_name = 'Olimpíada'
        verbose_name_plural = 'Olimpíadas'


class Competicao(Base):
    olimpiada = models.ForeignKey(Olimpiada, to_field='nome', null=False, on_delete=models.RESTRICT)
    esporte = models.CharField(max_length=40, blank=False)
    modalidade = models.CharField(max_length=100, blank=False)

    class Meta:
        models.UniqueConstraint(fields=['olimpiada', 'esporte', 'modalidade'], name='unique_competicao')
        verbose_name = 'Competição'
        verbose_name_plural = 'Competições'

    def __str__(self):
        return f'{self.olimpiada} - {self.esporte}, {self.modalidade}'


class CompeticaoAtleta(Base):
    competicao = models.ForeignKey(Competicao, null=False, on_delete=models.RESTRICT)
    atleta = models.ForeignKey(Atleta, null=False, on_delete=models.RESTRICT)
    idade_atleta = models.IntegerField(null=True)
    altura_atleta = models.DecimalField(null=True, decimal_places=2, max_digits=3)
    peso_atleta = models.DecimalField(null=True, decimal_places=2, max_digits=5)
    time = models.ForeignKey(Time, null=False, on_delete=models.RESTRICT,
                             default=94)
    medalha = models.CharField(max_length=6, choices=MEDALHA, blank=True)

