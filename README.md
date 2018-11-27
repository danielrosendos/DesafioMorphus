# Desafio Morphus

<p align="center">
  <a href="https://www.morphus.com.br">
    <img src="https://www.morphus.com.br/static/website/img/logo.png" alt="Logo Morphus">
  </a>

## Explicação do Desafio - Morphus:
- [Desafio Dev Team Morphus](#explicacaodesafio)

## Instalação dos Requisitos:
- [Django](#django)
- [Django Rest Framework](#djangorestframework)
- [Requests](#Requests)
- [Beautiful Soup](#soup)
- [Django Signals](#signals)
- [Celery](#celery)

## Implementação e Exeperiencia:
- [Implementacao](#implementacao)
- [Experiencia](#experiencia)

## Desafio Dev Team Morphus

Sistema para Monitoramento de dados de Filmes do IMDB

A Tarefa é criar uma API simples, apenas para consulta de dados, as informações devem ser obtidas realizando uma raspagem periódica, os dados podem ser obtidos no site https://www.imdb.com e devem ser armazenados em uma base de dados (Sqlite ou Postgresql) que vai ser a fonte da API.

Objetivo:

1 - O sistema deve ser alimentado com uma categoria de filme (Adventure, Family, Fantasy, ...).

2 - O sistema deve criar um processo periódico e assíncrono para cada categoria cadastrada, onde esse processo vai realizar a raspagem de dados da categoria configurada e trazer as informações dos filmes encontrados.

3 - O sistema deve oferecer uma API para consulta dos dados no seguinte padrão:

Ex:

    {

        "link": "https://www.imdb.com/title/tt4123430/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=ea4e08e1-c8a3-47b5-ac3a-75026647c16e&pf_rd_r=H00AR6RAYPKZ9R35D5FJ&pf_rd_s=center-1&pf_rd_t=15506&pf_rd_i=moviemeter&ref_=chtmvm_tt_1",

        "title":  "Animais Fantásticos: Os Crimes de Grindelwald",

        "year": "2018",

        "categories": ["Adventure", "Family", "Fantasy"],

        "director": "David Yates",

        ...

    }

4 - A API deve ser feita em Django, utilizando o Django rest framework

Observações:

1 - A configuração das categorias deve ser feita pelo Django Admin, utilizar o recurso Django Signals para acionar a task assíncrona.

2 - O sistema de tasks assíncronas, pode ser feito com as bibliotecas Celery e Celery Beat, Django crontab ou Scrapy.

3 - O sistema de varredura de dados pode ser feito utilizando as bibliotecas Requests e Beautiful Soup ou ferramentas do linux como o CURL, WGET e aplicar algumas consulta de strings ou regex.

4 - A entrega deve ser feita em algum repositório de sua preferencia e compartilhado o link por e-mail

Tecnologias:
- Python 3.5+
- Django, Django Signals
- Django Rest Framework
- Celery, Celery Beat, Django Crontab
- Request
- Beautiful Soup

## Django

Django é um framework para desenvolvimento rápido para web, escrito em Python, que utiliza o padrão model-template-view. Foi criado originalmente como sistema para gerenciar um site jornalístico na cidade de Lawrence, no Kansas. Tornou-se um projeto de código aberto e foi publicado sob a licença BSD em 2005

A instalação do django é bastante simples, dependendo da plataforma (Windows, Linux ou Mac) o comando pode ser diferente, no windows ajustado e configura o Path o comando é python, para outras plataformas é python3, já que utilizaremos o python 3.5+.

Para iniciar o django é preciso criar uma virtual env, então basta digitar o comando abaixo:

```
    windows: python -m venv venv
    linux/mac: python3 -m venv venv
```

Ative a virtual env

```
    windows: venv\Scripts\activate
    linux/mac: . venv/bin/activate
```

Ativada a virtual env, atualizamos o commando pip

```
    python -m pip install --upgrade pip
```

Por fim instalamos o django

```
    pip install django
```

E assim pode-se ser iniciado o projeto django usando o comando:

```
    django-admin startproject nomedoprojeto
```

<p align="center">
    <br>
    <a href="https://docs.djangoproject.com/pt-br/2.1/"><strong>Explore a Documentação do Django »</strong></a>
    <br>
    <br>
  </p>
</p>

## Django Rest Framework

A Django Rest Framework é uma blibioteca Django que viabiliza de forma simples a criação de APIS REST em projetos django usando de meios já conhecidos dos desenvolvedores para proporcionar produtividade na criação das APIS.

Com o django devidamente instalado e com a virtual env iniciada para instalar o django rest framework basta digitar no terminal o comando:

```
pip install djangorestframework
```

E referenciar o django dentro do settings do django

```
INSTALLED_APPS = (
    ...
    'rest_framework',
)
```

<p align="center">
    <br>
    <a href="https://www.django-rest-framework.org/"><strong>Explore a Documentação do Django rest Framework»</strong></a>
    <br>
    <br>
  </p>
</p>