# Toteutusdokumentti


## Ohjelman rakenne ja kuvaus 

### Algos-paketti
Paketti sisältää algoritmi X:n rajapinnan määrittelyn ja varsinaiset implementaatiot. Kummatkin algoritmit seuraavat samaa Algoritmi X:n perusajatusta, 
joka on pseudokoodina seuraava:
```
Jos annetussa matriisissa ei ole kolumneja, on löydetty ratkaisu.
Muuten: valitse sarakkeista c, jossa on vähiten alkioita.
Jokaista sarakkeen c riviä r kohtaan:
  Sisällytä r ratkaisuun
  Jokaiselle rivin r kolumnille j
    Jokaiselle kolumnin j riville t
      poista rivi t matriisista
  Käynnistä haku rekursiivisesti riisutulle matriisille
  Palauta poistetut rivit käänteisessä järjestyksessä
```

DLX -algoritmi perustuu Dancing links -tekniikkaan, jossa poistetaan ja palautetaan *"in-place"* kaksisuuntaisesti ja ympäri matriisin linkitettyjä solmuja 
(*"double linked circular linked lists"*). Solmut ovat siis muistissa algoritmin suorituksen ajan, jolloin poistettujen solmujen palauttaminen on tehokasta. 
Toteutus perustuu [Donald Knuthin artikkeliin vuodelta 2000](https://www.ocf.berkeley.edu/~jchu/publicportal/sudoku/0011047.pdf).

DictX -algoritmi perustuu hajautukseen, jossa kunkin kolumnin solmut on tallennettu dict / ja set-tietorakenteisiin. Näin sopivan kolumnin ja rivin löytäminen on nopeaa. 
Toteutus perustuu [Ali Assafin blogiin (vuosi tuntematon)](https://www.cs.mcgill.ca/~aassaf9/python/algorithm_x.html).

### Data creators -paketti
Paketti sisältää eri ongelmatyyppien ratkaisemiseen tarvittavat datan generoijat. 

Pentomino-moduuli toimii seuraavasti:
-  Ensin generoidaan sopiva universumi: yksi alkio jokaista pentominoa kohtaan, tunnisteena pentominon nimi ja yksi alkio jokaista mahdollista paikkaan kohtaan, tunnistetaana
paikan koordinaatti (x,y). Universumiin tulee siis 12 + 60 = 72 alkiota.
-  Seuraavaksi generoidaan joukko joukkoja universumin elementtejä. Jokaista pentominoa ja pentominojen kääntöjä kohtaan tehdään yksi kuuden alkion joukko: joukko sisältää 
   pentominon nimen sekä viisi koordinaattia, jotka peittyvät pentominon asettamisen myötä.
- Lopputuloksena syntyy matriisi, josta on mahdollista löytää täsmäpeite. Täsmäpeitteeseen kuuluu jokainen kahdestatoista pentominosta ja jokainen kuudestakymmenestä 
  peitetystä koordinaatista.
  
Sudoku-moduuli toimii seuraavasti:
- Ensin generoidaan sopiva universumi: neljä alkiota jokaista mahdollista laitettua numeroa kohtaan. Alkiot ovat laitetun numeron varaama koordinaatti (x,y), numeron varaama
  rivi, numeron varaama sarake sekä numeron varaama ruutu.
- Seuraavaksi generoidaan joukko joukkoja universumin elementeistä. Tässä käydään läpi annettu sudokulauta ja jokaista ruutua kohtaan generoidaan joko yksi tai yhdeksän joukkoa.
  Jos ruudussa on valmiiksi jokin numero, generoidaan vain yksi joukko sisältäen alkiot yllämainitulla tavalla. Muussa tapauksessa generoidaan yhdeksän joukkoa: yksi jokaista 
  mahdollista numeroa varten.
- Lopputuloksena syntyy matriisi, josta on mahdollista löytää täsmäpeite. Täsmäpeitteeseen kuuluu 81 riviä, joista jokainen kuvaa jonkin numeron sijoittamista johonkin 
  koordinaattiin siten, että sudokun säännöt on huomioitu.
 
### Datastructures-paketti 
Paketti sisältää ohjelman tarvitsemat itse tehdyt tietorakenteet:
- Matriisien rajapinta.
- Dancing links -toteutuksessa tarvitut linkitettyjen listojen erityyppiset solmut sekä matriisitoteutus, jonka metodeilla solmut liitetään yhteen
- Hajautustaulu-pohjainen matriisitoteutus, 
- Pentominojen esitys sekä kahdentoista pentominon yhteenkoonti

### Services-paketti
- Solver-moduuli toimii rajapinta käyttöliittymään ja mm. käynnistää datan generoinnin, algoritmit jne. sekä palauttaa löydetyt ratkaisut

### Translator-paketti
- Paketin ainoa moduuli sisältää toiminnallisuuden algoritmin löytämien ratkaisujen kääntämiseen ymmärrettävämpään muotoon eli valmiiksi pentomino-laudoiksi, sudoku-laudoiksi
tai ratkaisuun valittujen osajoukkojen listaksi
  
### UI
UI on toteutettu pienen python-serverin ja react-appin avulla. Kaikki ohjelman ominaisuudet eivät ole käytettävissä UI:n kautta, vain pentominojen ja sudokun ratkaiseminen.

# Saavutetut aika- ja tilavaativuudet

## Algoritmi X

### DLX

Analyysi perustuu enimmäkseen [David Eppsteinin blogiin vuodelta 2008](https://11011110.github.io/blog/2008/01/10/analyzing-algorithm-x.html).

Ohjelman pääalgoritmi toimii rekursiolla, ja jokaisella rekursiotasolla kutsut ovat toteutettujen tietorakenteiden ansiosta vakioaikaisia, 
joten saamme aikavaativuuden ylärajan seuraavasti: Olkoon `F` on joukko, jonka alkiot ovat joukkoja ja `F`:n alkioista voidaan rakentaa täsmällinen peite. 
Valitaan jokin `x` ja määritellään, että `C` on kaikkien niiden `F`:n alkioiden `S_i` joukko, joissa `x \in S_i`. 
Nyt algoritmi suorittaa `|C|` rekursiokutsua, joista jokaisella `F`:n koko on enimmillään `n - |C|`. Tästä saadaan ylärajaksi `O(3^(n/3)`.

Tilavaativuuden yläraja on `O(n)`, sillä linkitetyistä listoista koostettuun matriisiin tallennetaan ainostaan annettujen joukkojen elementtien kuvaus. Jokaista erillistä elementtiä kohtaan luodaan yksi kolumnisolmua ja jokaista elementtiä kohtaan luodaan yksi datasolmu. Esimerkiksi joukon `((1,2,4), (2,3,4))` kuvaamiseksi tarvitaan kuusi datasolmua sekä neljä kolumnisolmua.

## DictX

Toteutus toimii muuten samoin kuin DLX, mutta palautu

# Suorituskyky ja O-analyysivertailu

Linkitettyihin listoihin perustuva algoritmi suoriutuu ratkaisemisesta selvästi nopeammin kuin hajautustauluperustainen. Tämä johtunee... (analyysi seuraa). 


# Työn mahdolliset puutteet ja parannusehdotukset

- Hajautustaulupohjaista ratkaisua olisi todennäköisesti mahdollista optimoida vielä käyttämällä listoja aidon O(1) -pääsyn takaamiseksi hajautuksen keskimääräisen O(1) -pääsyn 
  sijaan
- Ohjelmaa olisi hyvä laajentaa mahdollisten syötteiden myötä
- Python on kielenä selvästi hitaammasta päästä, joten hajautustauluja sekä linkitettyjä listoja seuraava toteutus jollain low-level -kielellä voisi tuoda kiinnostavia 
  puolia esille

# Lähteet
- https://www.ocf.berkeley.edu/~jchu/publicportal/sudoku/0011047.pdf
- https://www.cs.mcgill.ca/~aassaf9/python/algorithm_x.html
- https://en.wikipedia.org/wiki/Exact_cover
- https://en.wikipedia.org/wiki/Knuth%27s_Algorithm_X
- https://en.wikipedia.org/wiki/Dancing_Links
- https://en.wikipedia.org/wiki/Pentomino
- http://www.tcs.hut.fi/Studies/T-79.5202/2006SPR/slideswww.pdf (suomenkielistä terminologiaa)
- https://boyetblog.s3.amazonaws.com/PCPlus/294.pentominoes.pdf