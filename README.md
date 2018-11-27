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

E referenciar o django rest dentro do settings do django

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

Após isso é instalado o django rest framework utilizando seus comando de instalação

```
pip install djangorestframework
```

E referenciar o django rest dentro do settings do django

```
INSTALLED_APPS = (
    ...
    'rest_framework',
)
```

E atualizamos nosso arquivos de url para termos os links e acessos a nossa api

```
from django.contrib import admin
from django.conf.urls import include
from rest_framework import routers
from django.urls import path
from categoriaIMDB.api.viewsets import CategoriasViewSet
from filmeCategoria.api.viewsets import FilmeCategoriaViewSet

router = routers.DefaultRouter()
router.register(r'categorias', CategoriasViewSet)
router.register(r'filme', FilmeCategoriaViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
```

Para cada APP criado (categoriaIMDB, filmeCategoria) criamos uma pasta api, onde lá teremos a estrutura de nossa api, onde será encontrado os arquivos serializers.py e viewsets.py

- categoria IMDB

```
#viewsets.py
from rest_framework.viewsets import ModelViewSet
from categoriaIMDB.models import Categorias
from .serializers import CategoriasSerializer

class CategoriasViewSet(ModelViewSet):
    queryset = Categorias.objects.all()
    serializer_class = CategoriasSerializer
```

Criação do viewset, onde as informação são puxadas e mostradas

```
##serializers.py
from rest_framework.serializers import ModelSerializer
from categoriaIMDB.models import Categorias

class CategoriasSerializer(ModelSerializer):
    class Meta:
        model = Categorias
        fields = [
            'id', 'categories'
        ]
```

Serialização onde decidimos quais campos serão mostrados e recuperados pela api

- filmeCategoria

```
#viewsets.py
from rest_framework.viewsets import ModelViewSet
from filmeCategoria.models import FilmeCategoria
from .serializers import FilmeCategoriaSerializer

class FilmeCategoriaViewSet(ModelViewSet):
    queryset = FilmeCategoria.objects.all()
    serializer_class = FilmeCategoriaSerializer
```

```
#serializers.py
from rest_framework.serializers import ModelSerializer
from filmeCategoria.models import FilmeCategoria

class FilmeCategoriaSerializer(ModelSerializer):
    class Meta:
        model = FilmeCategoria
        fields = [
            'link', 'title', 'year', 'categories', 'director', 'duration'
        ]
```

Interface da api pronta.

Para fazer a raspagem dos dados do IMDB utilizei Request e BeautifulSoup para este trabalho

```
from requests import get
from bs4 import BeautifulSoup
import re
import json
```

Bibliotecas importadas

Basicamente o algoritmo de raspagem dos dados começa da função abaixo:

```
def links(genrs):
    # url de inicio da varredura
    url = 'https://www.imdb.com/search/title?genres=fantasy&explore=title_type,genres&ref_=tt_ov_inf'
    response = get(url)
    html_soup = BeautifulSoup(response.text, 'html.parser')

    ##Pegando as categorias de filmes no site
    categoria_filmes = html_soup.find_all('div', class_='aux-content-widget-2')
    categoria_filmes = categoria_filmes[1].find_all('a')

    # Pegando o link da categoria
    for categoria in categoria_filmes:
        if categoria.text == genrs:
            link = categoria.attrs['href']

    # link da categoria
    url = 'https://www.imdb.com/' + link
    response = get(url)
    html_soup = BeautifulSoup(response.text, 'html.parser')
    mv_containers = html_soup.find_all('div', class_='lister-item mode-advanced')
    teste = html_soup.find('div', class_='desc')

    return json.dumps(dados(mv_containers, teste))
```

A função recebe o genero da categoria, inicia pela url onde do lado direito o IMDB faz a filtragem dos filmes ou series por genero, é coletado os textos e links dessa sessão do site, e é pecorrido por essa sessão, ao achar a sessão der match, pegamos o link da sessão e passamos essa sessão para ser recuperado esses dados, na função dados

```
def dados(mv_containers, teste):
    filme = {
        'link': 'string', 'title': 'string', 'year': 'int', 'categories': 'string',
        'director': 'string', 'duration': 'string'
    }

    info = []

    for x in range(1):
        for container in mv_containers:
            url = 'https://www.imdb.com/' + container.h3.a.attrs['href']
            response = get(url)
            soup = BeautifulSoup(response.text, 'html.parser')

            filme['link'] = url
            filme['title'] = container.h3.a.text
            filme['year'] = get_ano(soup)
            filme['categories'] = get_genero(soup)
            filme['director'] = get_diretor(soup)
            filme['duration'] = pegaDuracao(soup)

            info.append(filme)


        link = teste.find('a', class_='lister-page-next next-page')
        url = 'https://www.imdb.com/' + link.attrs['href']
        response = get(url)
        html_soup = BeautifulSoup(response.text, 'html.parser')
        mv_containers = html_soup.find_all('div', class_='lister-item mode-advanced')
        teste = html_soup.find('div', class_='desc')

    return info
```

Basicamente o que essa função faz é, pega o link do gereno escolhido, como por ex: https://www.imdb.com/search/title?genres=fantasy&genres=Fantasy&explore=title_type,genres&ref_=adv_explore_rhs, acessa filme por filme dessa seção e passa para a próxima página pegando link de filme por filme de cada sessão.
Ex: de link da proxima sessão https://www.imdb.com/search/title?genres=fantasy&start=51&explore=title_type,genres&ref_=adv_nxt, https://www.imdb.com/search/title?genres=fantasy&start=101&explore=title_type,genres&ref_=adv_nxt, mudando o numero da pagina 51 pra 101 e assim por diante. Claro que varrer tudo seria custoso, eu limitei para ir só até a segunda pagina. Caso quisesse que pecoresse tudo, basta no for primario pecorrer as páginas até que o botão next seja inexistente.

O link do filme já é pego pela url que é varrida, o titulo é pegado também pelo mesmo container.

O ano é pegado pela função ano:

```
def get_ano(soup):
    ano = soup.select("a[href*=/year/]")
    if len(ano):
        return int(ano[0].text)
    else:
        return None
```

Pegando a referencia pelo link que contenha a palavra year

Categoria é pego pela função get_genero

```
def get_genero(soup):
    genero = soup.find('div', {'id': 'titleStoryLine'})
    genero = genero.select("a[href*=/search/title?genres]")
    if genero != None:
        return [a.text for a in genero]
    else:
        return None
```

Onde ele pega a sessão storyline, e depois seleciona os textos que estão sendo registrados por title?genres

Diretor e pegar duração pelo mesmo principio

```
def get_diretor(soup):
    diretor = soup.find('div', attrs={'class': re.compile("^credit_summary_item")})
    diretor = [elemento.get_text() for elemento in diretor.find_all(re.compile(r'(a)'))]
    if diretor != None:
        return diretor
    else:
        return None


def pegaDuracao(soup):
    durFilme = soup.find('div', {'id': 'titleDetails'})
    durFilme = durFilme.find('time')
    if durFilme != None:
        string = durFilme.text
        return string
    else:
        return None
```

Por fim é retornado um json

Ainda faltou implementar algumas coisas como django signals e celery para as tasks assincronas. 


## Experiencia

Inicialmente gostaria de agradecer a morphus pela oportunidade, ganhei uma basta experiencia fazendo esse desafio, mesmo não estando 100% completo (até peço desculpas por não ter terminado 100%), mas consegui agregar muitos conhecimentos a qual eu não conhecia muito bem, foi bastante divertido quebrar a cabeça em como raspar os dados do site do IMDB, a criar aplicações django e rest api. Obiamente esse desafio continuarei estudando para completa-lo 100%, estudando e aprendendo. Novamente agradecer pela oportunidade é sempre bom estudar e agregar conhecimento, agradecer também ao Leonardo por ter dado também essa oportunidade. 

Não tinha muito conhecimento sobre django, conhecia claro a linguagem mas não muito especifico, mas com a vinda do desafio aprendi a utilizar a framework achei ela bastante versatil em relação a outras frameworks que utilizo atualmente (laravel), muito provavelmente começe a criar novos projetos utilizando a linguagem, criação de uma API, conhecia API somente pelos links de API coisas prontas, mas não em como construir uma, foi bastante interessante aprender a criar em partes uma API, e até como é simples entender o seu conceito e seu funcionamento e a parte que achei mais interessante, divertida e estressante foi a raspagem dos dados do site do IMDB, ter esse conhecimento me fez criar um novo leque de oportunidades para projetos futuros, até mesmo academicos para criação e analise de dados, utilizando já conhecimentos da cadeira de machine learn, então essa parte de como obter dados foi bastante boa para mim e por fim a parte que tive mais dificuldade foi no django signals e celery onde não entendi muito bem o seu funcionamento e como utilizar, mas continuo lendo e tentando aprender a utilizar.

E meus agradecimentos a todos da Morphus. 