from requests import get
from bs4 import BeautifulSoup
import re
import json

def get_ano(soup):
    ano = soup.select("a[href*=/year/]")
    if len(ano):
        return int(ano[0].text)
    else:
        return None


def get_genero(soup):
    genero = soup.find('div', {'id': 'titleStoryLine'})
    genero = genero.select("a[href*=/search/title?genres]")
    if genero != None:
        return [a.text for a in genero]
    else:
        return None


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
