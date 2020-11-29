# Toteutusdokumentti


## Ohjelman rakenne
- Ohjelma on jaettu seuraaviin paketteihin:
  - `algos`-paketti sisältää ohjelman algoritmit:
    - Algoritmi X:n rajapinnan määrittely, jonka kummatkin algoritmin implementaatiot toteuttavat
    - Dancing links (linkitetyt listat) -toteutus (nimeltään DLX) algoritmista. Toteutus perustuu [Donald Knuthin artikkeliin vuodelta 2000](https://www.ocf.berkeley.edu/~jchu/publicportal/sudoku/0011047.pdf).
    - Hajautusperustainen toteutus (nimeltään DictX) algoritmista. Toteutus perustuu [Ali Assafin blogiin (vuosi tuntematon)[https://www.cs.mcgill.ca/~aassaf9/python/algorithm_x.html]
  - `data_creators`-paketti sisältää eri ongelmatyyppien ratkaisemiseen tarvittavan datan generoijat:
    - Rajapinnan määrittely: kaikkien rajapintojen tulee generoida sopiva __universumi__ sekä __kokoelma joukkoja__, joista koostetaan universumin täsmäpeite kaikilla mahdollisilla tavoilla. Nämä yhdessä rajoittavat täsmäpeitteen etsinnän.
    - Geneerinen datan generoija: tekee annetuista merkkijonoista sopivat datat.
    - Pentomino-datan generoija: tekee annetun pentomino-laudan koon mukaan sopivan datan
  - `datastructures`-paketti sisältää ohjelman tarvitsemat itse tehdyt tietorakenteet:
    - Dancing links -toteutuksessa tarvitut linkitettyjen listojen erityyppiset solmut sekä matriisitoteutus, jonka metodeilla solmut liitetään yhteen
    - Hajautustaulu-pohjainen matriisitoteutus
    - Pentominojen esitys kaksiulotteisena listoina
  - `ui` -paketti sisältää käyttöliittymän
  - `services`- -paketti sisältää sovelluslogiikan:
    - solver-moduuli toimii rajapinta käyttöliittymään ja mm. käynnistää datan generoinnin, algoritmit jne. sekä palauttaa löydetyt ratkaisut
    - pentomino_browser -moduuli palautetaan solver-moduulin käyttäjälle ja sen avulla voi selata generoituja pentomino-ratkaisuja.

## Saavutetut aika- ja tilavaativuudet

Analyysi perustuu enimmäkseen [David Eppsteinin blogiin vuodelta 2008](https://11011110.github.io/blog/2008/01/10/analyzing-algorithm-x.html)

Ohjelman pääalgoritmi toimii rekursiolla, jajokaisella rekursiotasolla kutsut ovat toteutettujen tietorakenteiden ansiosta vakioaikaisia, joten saamme aikavaativuuden ylärajan seuraavasti: Olkoon `F` on joukko, jonka alkiot ovat joukkoja ja `F`:n alkioista voidaan rakentaa täsmällinen peite. Valitaan jokin `x` ja määritellään, että `C` on kaikkien niiden `F`:n alkioiden `S_i` joukko, joissa `x \in S_i`. Nyt algoritmi suorittaa `|C|` rekursiokutsua, joista jokaisella `F`:n koko on enimmillään `n - |C|`. Tästä saadaan ylärajaksi `O(3^(n/3)`.

Tilavaativuuden yläraja on `O(n)`, sillä linkitetyistä listoista koostettuun matriisiin tallennetaan ainostaan annettujen joukkojen elementtien kuvaus. Jokaista erillistä elementtiä kohtaan luodaan yksi kolumnisolmua ja jokaista elementtiä kohtaan luodaan yksi datasolmu. Esimerkiksi joukon `((1,2,4), (2,3,4))` kuvaamiseksi tarvitaan kuusi datasolmua sekä neljä kolumnisolmua.

# Suorituskyky ja O-analyysivertailu

Linkitettyihin listoihin perustuva algoritmi suoriutuu ratkaisemisesta selvästi nopeammin kuin hajautustauluperustainen. Tämä johtunee... (analyysi seuraa). 


# Työn mahdolliset puutteet ja parannusehdotukset

- Python on kielenä selvästi hitaammasta päästä, joten hajautustauluja sekä linkitettyjä listoja seuraava toteutus jollain low-level -kielellä voisi tuoda kiinnostavia puolia esille
- Graafisessa puolessa on parannettavaa

# Lähteet
- https://www.ocf.berkeley.edu/~jchu/publicportal/sudoku/0011047.pdf
- https://www.cs.mcgill.ca/~aassaf9/python/algorithm_x.html

- https://en.wikipedia.org/wiki/Exact_cover
- https://en.wikipedia.org/wiki/Knuth%27s_Algorithm_X
- https://en.wikipedia.org/wiki/Dancing_Links
- https://en.wikipedia.org/wiki/Pentomino
- http://www.tcs.hut.fi/Studies/T-79.5202/2006SPR/slideswww.pdf (suomenkielistä terminologiaa)
- https://boyetblog.s3.amazonaws.com/PCPlus/294.pentominoes.pdf
