# Desafio Morphus

<p align="center">
  <a href="https://www.morphus.com.br">
    <img src="https://www.morphus.com.br/static/website/img/logo.png" alt="Logo Morphus">
  </a>

## Explicação do Desafio - Morphus:
- [Desafio Dev Team Morphus](#Desafio Dev Team Morphus)

## Instalação Django e Django Rest Framework:
- [Django](#django)
- [Django Rest Framework](#Django Rest Framework)

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

## Implementação

Como principio, foi instalado o framework Django, na pasta do projeto DesafioMorphus2.0:

```
Instalando a virtual env: python -m venv venv
Iniciando a virtual env: venv\Script\Activate
Atualizando o pip: python -m pip install --upgrade pip
Instalando o django: pip install django
Iniciando o projeto: django-admin startproject DesafioMorphus .
```

A partir dai é feita as migrations para ser criado o banco sqlite e inicialização do server para saber se tudo está funcionando

```
makemigrations: python manage.py makemigrations
migrate: python manage.py migrate
runserver: python manage.py runserver
```

O servidor é iniciado no localhost porta 8000, caso tudo esteja funcionando apareceça a tela inicial do django.

A Partir dai começamos a criar nossos modelos, o categoria IMDB e filmeCategoria, o categoriaIMDB servirá como o inicializador, lá será onde adicionaremos nossas categorias e no filmeCategoria será onde os filmes peggados do IMDB seram salvos.

```
categoriaIMDB: python manage.py startapp categoriaIMDB
filmeCategoria: python manage.py startapp filmeCategoria
```

Adicionamos esses dois apps no settings do django

```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'categoriaIMDB',
    'filmeCategoria',
]
```

- Model categoriaIMDB: O nosso modelos é bem simples e é feito da seguinte forma

```
from django.db import models
from django.contrib.auth.models import User

class Categorias(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    categories = models.CharField(max_length=150)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.categories
```

Possui o usuario que adiciona, a categoria que queremos colocar e a data que foi adicionada de forma de auto incrementada. E adicionamos esse novo model em admin.py da pasta categoriaIMDB

```
from django.contrib import admin
from .models import Categorias

admin.site.register(Categorias)
```

- filmeCategoria:

O modelos é composto da seguinte forma:

```
from django.db import models

class FilmeCategoria(models.Model):
    link = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    year = models.CharField(max_length=255)
    categories = models.CharField(max_length=255)
    director = models.CharField(max_length=150)
    duration = models.CharField(max_length=150)

    def __str__(self):
        return self.title
```

Composto pelo link do filme, o titulo, o ano do filme, a categoria do filme, o diretor do filme e a duraçao do filme. E é adicionado também no arquivo admin, para o painel django admin encontrar nosso modelos

```
from django.contrib import admin
from .models import FilmeCategoria

admin.site.register(FilmeCategoria)
```

Feito isso, damos um novo makemigrations e migrate e criaremos um usuario admin para podermos ter acesso ao djago admin

```
python manage.py createsuperuser
```

Com isso nossa interface básica já esta criada para adicionarmos novas categorias e novos filmes.
