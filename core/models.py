from django.db import models

# Create your models here.
# class Question(models.Model):
#    question_text = models.CharField(max_length=200)
#    pub_date = models.DateTimeField('date published')

# [id_facu] [numeric](18, 0) IDENTITY(1,1) NOT NULL,
# [nome_facu] [varchar](100) NOT NULL,
# [sigla_facu] [varchar](20) NOT NULL,
# [n0800_facu] [varchar](20) NULL,
# [logotipo_facu] [image] NULL,
# [logomarca_facu] [image] NULL,
# [endereco_facu] [varchar](200) NOT NULL,

class Faculdade(models.Model):
    nome_facu = models.CharField(max_length=100)
    sigla_facu = models.CharField(max_length=20)
    n0800_facu = models.CharField(max_length=20)
    logotipo_facu = models.ImageField
    logomarca_facu = models.ImageField
    endereco_facu = models.CharField(max_length=200)


#[id_curs][numeric](18, 0) IDENTITY(1, 1) NOT NULL,
#[id_facu_curs][numeric](18, 0)NOT NULL,
#[nome_curs][varchar](50) NOT NULL,
#[sigla_curs][varchar](10) NOT NULL,
##[grau_curs][varchar](20) NOT NULL,
#[autorizacao_reconhecimento_curs][varchar](30) NULL, \
#[duracao_curs][varchar](20) NULL,  \
#[situacao_curs][bit] NOT NULL,

class Curso(models.Model):
    id_facu_curs = models.ForeignKey(Faculdade, on_delete=models.CASCADE)
    nome_curs = models.CharField(max_length=50)
    sigla_curs = models.CharField(max_length=10)
    grau_curs = models.CharField(max_length=20)
    autorizacao_reconhecimento_curs = models.CharField(max_length=30)
    duracao_curs = models.CharField(max_length=20)
    situacao_curs = models.BinaryField


#   [id_facu_prse] [numeric](18, 0) NOT NULL,
#	[nome_prse] [varchar](100) NOT NULL,
#	[nome_abreviado_prse] [varchar](20) NOT NULL,
#	[sigla_prse] [varchar](10) NOT NULL,
#	[id_ques_prse]

class Seletivo(models.Model):
    id_facu_prse = models.ForeignKey(Faculdade, on_delete=models.CASCADE)
    nome_prse = models.CharField(max_length=100)
    nome_abreviado_prse = models.CharField(max_length=20)
    sigla_prse = models.CharField(max_length=10)
    #id_ques_prse = models.ForeignKey(Questionario, on_delete=models.CASCADE)



