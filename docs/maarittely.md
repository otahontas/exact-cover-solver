# Määrittelydokumentti

## Mitä algoritmeja ja tietorakenteita toteutat työssäsi

Toteutan Algoritmi X:n eli rekursiivisen ja ei-deterministisen peruuttavan haun algoritmin täsmällisen peitteen (*exact cover*) löytämiseksi. 
Algoritmi toteutetaan kahdella eri tavalla: toinen dancing links -tekniikan avulla ja toinen hajautukseen perustuvien pythonin set- ja dictionary-rakenteiden avulla. Dancing links -tekniikaassa käytetään kahteen suuntaan linkitettyjä listoja (*doubly linked list*). 

## Mitä ongelmaa ratkaiset ja miksi valitsit kyseiset algoritmit/tietorakenteet

Täsmällisen peitteen ongelma on NP-täydellinen päätösongelma ja siten pelkällä koko ratkaisuavaruuden läpikäynnillä algoritmit (esimerkiksi peruuttava haku) ovat varmasti hitaita jo pienillä syötteillä. Dancing links ja algorihm X vaikuttavat mielenkiintoisilta lähestymistavoilta ongelmaan, nopeuttavat lukemani perusteella ratkaisun löytämistä huomattavasti ja niihin liittyvästä teoriasta löytyy hyviä artikkeleita.

## Mitä syötteitä ohjelma saa ja miten näitä käytetään

Ohjelmassa on kolme eri tyyppistä syötemahdollisuutta:
1. Erilaisten pentominojen (koot 6×10, 5×12, 4×15 and 3×20) ratkaisujen löytäminen: esim. yksittäisen ratkaisun palauttaminen tai kaikkien mahdollisten ratkaisujen lukumäärän laskeminen
2. Sudokujen ratkaisujen löytäminen
3. Täsmäpeitteen löytäminen suoraan syötteestä, jossa annetaan universumi ja joukko universumin elementeistä koostettuja osajoukkoja.

## Tavoitteena olevat aika- ja tilavaativuudet (m.m. O-analyysit)

Tavoitteena on siis toteuttaa algoritmi, joka etsii kaikki mahdolliset peitteet. Dancing links -tekniikan avulla toimet jokaisella rekursiotasolla ovat vakioaikaisia, joten saamme aikavaativuuden ylärajan seuraavasti: Olkoon `F` on joukko, jonka alkiot ovat joukkoja ja `F`:n alkioista voidaan rakentaa täsmällinen peite. Valitaan jokin `x` ja määritellään, että `C` on kaikkien niiden `F`:n alkioiden `S_i` joukko, joissa `x \in S_i`. Nyt algoritmi suorittaa `|C|` rekursiokutsua, joista jokaisella `F`:n koko on enimmillään `n - |C|`. Tästä saadaan ylärajaksi `O(3^(n/3)`.

## Lähteet
- https://www.ocf.berkeley.edu/~jchu/publicportal/sudoku/0011047.pdf
- https://11011110.github.io/blog/2008/01/10/analyzing-algorithm-x.html
- https://en.wikipedia.org/wiki/Exact_cover
- https://en.wikipedia.org/wiki/Knuth%27s_Algorithm_X
- https://en.wikipedia.org/wiki/Dancing_Links
- https://en.wikipedia.org/wiki/Pentomino
- http://www.tcs.hut.fi/Studies/T-79.5202/2006SPR/slideswww.pdf (suomenkielistä terminologiaa)
- https://boyetblog.s3.amazonaws.com/PCPlus/294.pentominoes.pdf

## Muut tiedot
- Opinto-ohjelma: tietojenkäsittelytieteen kandidaatti
- Dokumentaatiokieli: suomi, pois lukien committeja, jotka hyvän tavan mukaisesti englanniksi
- Ohjelman kieli: python