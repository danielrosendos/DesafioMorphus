# Desafio Morphus

<p align="center">
  <a href="https://www.morphus.com.br">
    <img src="https://www.morphus.com.br/static/website/img/logo.png" alt="Logo Morphus">
  </a>

## Explicação do Desafio - Morphus:
- [Desafio Dev Team Morphus](#explicacaodesafio)

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

