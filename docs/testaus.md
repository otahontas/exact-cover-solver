# Testausdokumentti

Projektin testit koostuvat yksittäisiä luokkia ja luokkien metodeja testaavista yksikkötesteistä sekä ohjelman toiminnallisuutta kokonaisuudessaan testaavista suorituskykytesteistä. 
Testeissä on huomioitu myös tulosten oikeellisuuden tarkistus - erillisiä "hyväksymistestejä" ei ole näin ollen laadittu.


## Yksikkötestit

Yksikkötestit on laadittu erikseen jokaiselle luokalle ja testikattavuus on pyritty pitämään yli 90 prosentissa. Seuraavat asiat ovat olennaisimpia testattuja asioita:
- Algoritmi X:n implementaatiot: löytääkö implementaatio oikeat tulokset annetulla matriisilla? Valitseeko implementaatio järkevästi optimimaalisimman kolumnin tutkittavaksi?
- Datan generointi: tuottaako datan generoija oikeanlaista dataa eli onko annettu ongelma käännetty oikein täsmäpeiteongelmaksi? Tuotetaanko esimerkiksi oikeat rivit sudokua varten ja
  käytetäänkö pentominoja oikein?
- Tietorakenteet: toimivatko yksinkertaiset tietorakennetoteutukset oikein?
- services / translator: Palautetaanko algoritmeista saatu ratkaisudata oikeassa muodossa käyttäjälle?

Yksikkötesteissä käytetään melko pieniä syötteitä (n < 10), jotta testien ajaminen on jouhevaa. 

Yksikkötestit voi ajaa README:n ohjeiden mukaisesti joko poetryn asennuksen jälkeen `poetry run invoke test` tai dockerilla 
`docker build . -t exact-cover-solver-dev -f Dockerfile-dev && docker run -it -v $(pwd):/app exact-cover-solver-dev test`.

## Suorituskykytestit

Suorituskykytesteissä testataan ohjelman toimintaan isoilla hakuavaruuksilla. Syötteen koot ja rakenne vaikuttavat erityisesti ohjelman
rekursiotasojen määrään sekä mahdollisuuksiin karsia haara hakupuusta mahdollisimman aikaisin. Testejä on kolmea eri tyyppiä ja ne ajetaan kumpaakin algoritmin implementaatiota vasten.
Testit raportoivat tulokset simppelisti tekstimuotoisena, josta niitä voi vertailla.

Suorituskykytestit voi ajaa yksinkertaisesti komennolla `pypy3 performance_tests/main.py` tai dockerilla: docker build . -t exact-cover-solver-perf-tests -f Dockerfile-perf-tests && docker run exact-cover-solver-perf-tests

### Pentomino-laudat

Pentomino-lautojen ratkaisuja etsitään neljästä eri kokoisesta laudasta: 3x20, 4x15, 5x12, 6x10. Kaikissa ongelmissa annetun syötteen koko on melko samaa luokkaa.
Käytettävässä matriisissa on aina 72 saraketta, ja rivejä on 1182, 1618, 1846 tai 1960 kpl. Syötteen koko vaihtelee siis välillä 85000 - 140000, eli n. 10^5. Ratkaisujen koot vaihtelevat, 
mistä algoritmin ajojen kesto.

### Sudoku-laudat

Sudoku-lautojen ratkaisuja etsitään myös neljällä erilaisella laudalla, joissa vihjeiden eli valmiiksi annettujen numeroiden ja siten myös ratkaisujen määrä vaihtelee. 
Helpoin sudoku on yhden ratkaisun sudoku, vaikeimmassa on yli miljoona mahdollista ratkaisua. Ratkaisujen määrä on pyritty vahvistamaan netistä löytyvillä työkaluilla 
(esim. https://www.thonky.com/sudoku/solution-count), mutta muiden työkalujen toimintavarmuus vaihtelee. Tähän ei siis ole löydetty hirveän tyydyttävää ratkaisua, joten 
olen pyrkinyt luottamaan siihen, että pienten syötteiden oikea ratkaisujen määrä takaisi saman myös isoille syötteille.

### Testit suoraan annetuilla universumi - ja osajoukkokokoelmilla

Kolmannessa testityypissä ohjelmalle annetaan jokin n ja m, jossa n on universumin koko
ja m kerroin, jonka mukaan osajoukkokokoelmaan laitetaan osajoukkoja m * 10 kpl. Tässä
n vaikuttaa erityisesti muodostuvan matriisin sarakkeiden määrään ja m mahdollisten
ratkaisujen määrään.

Käytetyt m ja n:
- n: 100, 1000, 10000
- m: 1,2,3,4

Näistä viimeisin tuottaa matriisin, jossa on 400000 alkiota ja ratkaisuita 4 ** 10. Tämä
on melko lailla säädyllinen yläraja, jonka jälkeen käytössä olleen tietokoneen
suorituskykyrajat tulevat vastaan.