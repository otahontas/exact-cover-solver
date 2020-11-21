# Exact cover solver

[![Tests](https://github.com/otahontas/exact-cover-solver/workflows/Tests/badge.svg)](https://github.com/otahontas/exact-cover-solver/actions?query=workflow%3ATests)
[![Coverage](https://coveralls.io/repos/github/otahontas/exact-cover-solver/badge.svg?branch=master)](https://coveralls.io/github/otahontas/exact-cover-solver?branch=master)
[![Code style](https://github.com/otahontas/exact-cover-solver/workflows/Code%20style/badge.svg)](https://github.com/otahontas/exact-cover-solver/actions?query=workflow%3A%22Code+style%22)
[![Docs](https://github.com/otahontas/exact-cover-solver/workflows/Docs/badge.svg)](https://github.com/otahontas/exact-cover-solver/actions?query=workflow%4ADocs)

Project for Helsinki University's Data structures and algorithms -project course. Repository docs are written in Finnish.

## Dokumentaatio
- [Määrittelydokumentti](docs/maarittely.md)
- [Testikattavuusraportti](https://coveralls.io/github/otahontas/exact-cover-solver?branch=master)
- [Koodin dokumentaatio](https://otahontas.github.io/exact-cover-solver/)

## Viikkoraportit
- [Viikko 1](docs/raportit/viikko1.md)
- [Viikko 2](docs/raportit/viikko2.md)
- [Viikko 3](docs/raportit/viikko3.md)

## Käyttöohje

Ohjelmistovaatimukset:
- `Pypy 3.7+` / `Python 3.6+`. 
  - Koska ohjelma on toteutettu puhtaasti pythonilla, Pypyn käyttö parantaa ohjelman suorituskykyä huomattavasti. Esimerkiksi vastausten lukumäärän etsiminen [pentomino-pelissä](https://en.wikipedia.org/wiki/Pentomino) 6x10-kokoisen ruudukolla kestää Pypyllä n. 30 sek ja cpythonilla n. 10 minuuttia (Intel 3.4Ghz i5 cpu:lla)
  - Pypyn voit ladata [projektin nettisivuilta](https://www.pypy.org/download.html), [pyenvin avulla](https://github.com/pyenv/pyenv) tai todennäköisesti käyttöjärjestelmäsi paketinhallinnasta.

Voit asentaa ja käynnistää ohjelman melko yksinkertaisesti ilman kehittäjätyökaluja seuraavasti (korvaa komennoissa oleva `pypy3` komennolla `python3`, jos et halua / voi käyttää pypyä):
- Tee virtuaaliympäristö ajamalla `pypy3 -m venv venv` (tai `python3 -m venv venv`)
- Ota virtuaaliympäristö käyttöön `source venv/bin/activate`
- Päivitä pip: `pypy3 -m pip install --upgrade pip`
- Asenna ohjelma `pypy3 -m pip install .`
- Käynnistä ohjelma `pypy3 exact_cover_solver/main.py`
- Voit vaihtoehtoisesti ajaa pelkästään ohjelman suorituskykytestit komennolla `pypy3 performance_tests/test_pentominoes_with_dlx.py`

## Kehittäminen
Ohjelmistovaatimukset:
- `Poetry 1.0+`, 
  - Poetryn asennusohjeet ja -skripti löytyvät [projektin sivuilta](https://python-poetry.org/docs/#installation).
- (Suositeltava): `pyenv` helpottaa python-versioiden hallinnassa
  - Pyenvin asennusohjeet ja -skripti [projektin githubista](https://github.com/pyenv/pyenv)

### Asennus
Asenna projektin tarvitsemat paketit komennolla `poetry install`. Tämän jälkeen voit käyttää [invoken](https://www.pyinvoke.org/) avulla tehtyjä skriptejä. Skriptit saat esille myös ajamalla `poetry run invoke --list`.

### Käynnistys
Käynnistä ohjelma komennolla:

```
poetry run invoke start
```

### Testit

Aja testit komennolla:

```
poetry run invoke test
```

Komento printtaa yleisen koodikattavuusraportin terminaaliin. Tarkemman, html-muotoisen raportin saat ajamalla `poetry run invoke cov`, minkä jälkeen raportti löytyy polusta `htmlcov/index.html`.

### Koodityylit


Tarkista koodityylit komennolla:

```
poetry run invoke lint
```

Koodityylit tarkistetaan [flake8](https://flake8.pycqa.org/en/latest/index.html) - ja [black](https://black.readthedocs.io/en/stable/) -työkaluilla. Tarkemmin nämä sisältävät tarkistukset:
- [pep8-tyyliohjeiden](https://www.python.org/dev/peps/pep-0008/) noudattamisesta
- virheistä, turhista importeista jne
- koodin liiallisesta haarautumisesta / kompleksisuudesta
- black-formatoijan tyyliohjeiden noudattamisesta
- [pep257 -docstring ohjeiden](https://www.python.org/dev/peps/pep-0257/) noudattamisesta (vain lähdekoodille, testeille ei ajeta docstring-tarkastuksia)

Blackin huomaamat virheet voi korjata automaattisesti ajamalla `poetry run invoke list`. Flaken huomaamat virheet täytyy sen sijaan korjata käsin.

### API-dokumentaatio

Generoi ohjelman sisäinen dokumentaatio (vrt. Javadocit) komennolla:

```
poetry run invoke docs
```

Tämän jälkeen [pdoc-kirjastolla](https://pdoc3.github.io/pdoc/) generoitu html-muotoinen dokumentaatio löytyy polusta `docs/index.html`.
