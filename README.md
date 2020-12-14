# Exact cover solver

[![Tests](https://github.com/otahontas/exact-cover-solver/workflows/Tests/badge.svg)](https://github.com/otahontas/exact-cover-solver/actions?query=workflow%3ATests)
[![Coverage](https://coveralls.io/repos/github/otahontas/exact-cover-solver/badge.svg?branch=master)](https://coveralls.io/github/otahontas/exact-cover-solver?branch=master)
[![Code style](https://github.com/otahontas/exact-cover-solver/workflows/Code%20style/badge.svg)](https://github.com/otahontas/exact-cover-solver/actions?query=workflow%3A%22Code+style%22)
[![Docs](https://github.com/otahontas/exact-cover-solver/workflows/Docs/badge.svg)](https://github.com/otahontas/exact-cover-solver/actions?query=workflow%4ADocs)
[![Performance tests](https://github.com/otahontas/exact-cover-solver/workflows/Performance%20tests/badge.svg)](https://github.com/otahontas/exact-cover-solver/actions?query=workflow%3A%22Performance+tests%22)

Project for Helsinki University's Data structures and algorithms -project course. Repository docs are written in Finnish.

Exact cover solver -kirjasto ratkoo np-täydellisen täsmäpeiteongelman sekä täsmäpeiteongelmaksi kääntyviä ongelmia, mm. pentomino-pelejä. Ohjelmassa on toteutettu Donald Knuthin Algorithm X dancing links- ja hajautuspohjaisella implementaatiolla.

## Dokumentaatio

- [Määrittelydokumentti](docs/maarittely.md)
- [Testausdokumentti](docs/testaus.md)
- [Toteutusdokumentti](docs/toteutus.md)
- [Testikattavuusraportti](https://coveralls.io/github/otahontas/exact-cover-solver?branch=master)
- [Koodin dokumentaatio](https://otahontas.github.io/exact-cover-solver/)

## Viikkoraportit

- [Viikko 1](docs/raportit/viikko1.md)
- [Viikko 2](docs/raportit/viikko2.md)
- [Viikko 3](docs/raportit/viikko3.md)
- [Viikko 4](docs/raportit/viikko4.md)
- [Viikko 5](docs/raportit/viikko5.md)
- [Viikko 6](docs/raportit/viikko6.md)

## Käyttöohje

(Tulossa)

## Kehittäminen

- Kloonaa repo, siirry repon juureen

### Docker

- Rakenna kehitysympäristö docker-imageen komennolla: `docker build . -t exact-cover-solver-dev -f Dockerfile-dev`
- Käynnistä docker-container ajamalla `docker run -it -v $(pwd):/app exact-cover-solver-dev` ja saat listan sopivista komennoista. Repon kansio kiinnitetään dockeriin, jotta mahdolliset muutokset (coverage tms) päivttyvät kansioon.
- Komentoja käytetään argumenttina edelliseen eli `docker run -v $(pwd):/app exact-cover-solver-dev <komento>`.
- Suorituskykytestit tulee ajaa pypyllä. Ympäristön tähän voit rakentaa ja testit ajaa seuraavasti:

```
docker build . -t exact-cover-solver-perf-tests -f Dockerfile-perf-tests && docker run exact-cover-solver-perf-tests
```

### Ilman Dockeria

Huolehdi, että vaaditut ohjelma on asennettu:

- Vähintään `Python 3.6.9` sekä `pypy3.6-7.3.1`
  - Ohjelma on toteutettu pythonin standardikirjastolla, joten pypyn käyttö parantaa ohjelman suorituskykyä huomattavasti, jopa 20-kertaisesti. Suorituskykytestit ajetaankin vain pypyä vasten.
  - Jos sinulla ei ole sopivia versioita, voit joko:
    - asentaa pypyn [pypy.org -sivulta](https://www.pypy.org/download.html) ja pythonin [python.org -sivulta](https://www.python.org/downloads/) tai
    - asentaa pypyn ja pythonin eri versiot käyttöjärjestelmäsi paketinhallinnasta (`brew, apt-get...` jne) tai
    - asentaa [pyenvin](https://github.com/pyenv/pyenv) ja ajaa asennuksen jälkeen repon juuressa `pyenv install 3.6.9` sekä `pyenv install pypy3.6-7.3.1`. Ota sitten versiot käyttöön ajamalla `pyenv local 3.6.9 pypy3.6-7.3.1`.
- [Poetry 1.1+](https://python-poetry.org/docs/#installation), jonka voit asentaa monella eri tapaa, ks. linkatut ohjeet. Jos käytät pyenviä, poetry käyttää automaattisesti oikeaa versiota. Muussa tapauksessa joudut asettamaan version ajamalla projektin juuressa `poetry use 3.6.9`.

Asennettuasi projektin tarvitsemat paketit jommalla kummalla tavalla, voit käyttää [invoken](https://www.pyinvoke.org/) avulla tehtyjä skriptejä. Skriptit saat esille myös ajamalla `poetry run invoke --list` (tai dockerilla yllä mainitulla komennolla).

### Testit

Aja testit komennolla:

```
poetry run invoke test
```

Komento printtaa yleisen koodikattavuusraportin terminaaliin. Tarkemman, html-muotoisen raportin saat ajamalla `poetry run invoke cov`, minkä jälkeen raportti löytyy polusta `htmlcov/index.html`.

### Suorituskykytestit

(Seuraa myöhemmin)

### Koodityylit

Tarkista koodityylit ja tyypitykset komennolla:

```
poetry run invoke lint
```

Koodityylit ja tyypitykset tarkistetaan [flake8](https://flake8.pycqa.org/en/latest/index.html) -, [black](https://black.readthedocs.io/en/stable/) ja [mypy](http://mypy-lang.org/) -työkaluilla. Tarkemmin nämä sisältävät tarkistukset:

- [pep8-tyyliohjeiden](https://www.python.org/dev/peps/pep-0008/) noudattamisesta
- virheistä, turhista importeista jne
- koodin liiallisesta haarautumisesta / kompleksisuudesta
- black-formatoijan tyyliohjeiden noudattamisesta
- [Google Python Style Guiden](https://www.python.org/dev/peps/pep-0257/) noudattamisesta docstringeissä (vain lähdekoodille, testeille ei ajeta docstring-tarkastuksia)
- virheistä staattisen tyypityksen kanssa

Blackin huomaamat virheet voi korjata automaattisesti ajamalla `poetry run invoke list`. Flaken ja mypyn huomaamat virheet täytyy sen sijaan korjata käsin.

### API-dokumentaatio

Ohjelman sisäisessä dokumentaatiossa (docstringit) käytetään [Googlen Python Style Guide](https://google.github.io/styleguide/pyguide.html) -konventiota.

Generoi dokumentaatio (vrt. Javadocit) komennolla:

```
poetry run invoke docs
```

Tämän jälkeen [pdoc-kirjastolla](https://pdoc3.github.io/pdoc/) generoitu html-muotoinen dokumentaatio löytyy polusta `docs/index.html`.
