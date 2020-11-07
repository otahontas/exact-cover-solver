# Exact cover solver

Project for Helsinki University's Data structures and algorithms -project course. Repository docs are written in Finnish.

## Dokumentaatio
- [Määrittelydokumentti](dokumentaatio/maarittely.md)

## Viikkoraportit
- [Viikko 1](dokumentaatio/raportit/viikko1.md)

## Käyttöohje

Ohjelmistovaatimukset:
- `Python 3.8+`
- `Pipenv`, joko `pip`:n tai järjestelmän paketinhallinnan kautta asennettuna. Asennuksesta lisää [ohjelmistotekniikan kurssimateriaalista](https://github.com/ohjelmistotekniikka-hy/python-syksy-2020/blob/master/materiaali/pipenv.md)

Dokumentaatiossa käytetään pipenvin ajamiseen komentoa `pipenv run ...`. Korvaa se muodolla `python3 -m pipenv run ...`, jos pip:n asennukset eivät mene `$PATH`-polkuusi.

### Käynnistys
Käynnistä ohjelma ajamalla:

```
pipenv run start
```


### Koodityylit

Ohjelman koodityylit voit tarkistaa ajamalla

```
pipenv run lint
```

Koodityylit tarkistetaan [flake8](https://flake8.pycqa.org/en/latest/index.html)- ja [black](https://black.readthedocs.io/en/stable/)-työkaluilla. Tarkemmin nämä sisältävät tarkistukset:
- [pep8-tyyliohjeiden](https://www.python.org/dev/peps/pep-0008/) noudattamisesta
- virheistä, turhista importeista jne
- koodin liiallisesta haarautumisesta / kompleksisuudesta
- black-formatoijan tyyliohjeiden noudattamisesta
- [pep257 -docstring ohjeiden](https://www.python.org/dev/peps/pep-0257/) noudattamisesta (vain lähdekoodille, testeille ei ajeta docstring-tarkastuksia)

Blackin huomaamat virheet voi korjata automaattisesti ajamalla `pipenv run format`. Flaken huomaamat virheet täytyy sen sijaan korjata käsin.
