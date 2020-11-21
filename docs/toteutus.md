# Toteutusdokumentti


## Ohjelman rakenne
- Ohjelma on jaettu seuraaviin paketteihin:
  - `algos`-paketti sisältää ohjelman algoritmit:
    - Algoritmi X:n rajapinnan määrittely
    - Dancing links (linkitetyt listat) -toteutus (nimeltään DLX) algoritmista
  - `datastructures`-paketti sisältää ohjelman tarvitsemat itse tehdyt tietorakenteet:
    - Dancing links -toteutuksessa tarvitut linkitettyjen listojen erityyppiset solmut sekä matriisitoteutus, jonka metodeilla solmut liitetään yhteen
  - `ui` -paketti sisältää käyttöliittymän
  - `services`- -paketti sisältää sovelluslogiikan:
    - `solver`-moduuli toimii rajapinta käyttöliittymään ja mm. käynnistää datan generoinnin, algoritmit jne.
  - `utils` -paketti sisältää apuluokkia datan generointiin

## Saavutetut aika- ja tilavaativuudet

Ohjelman pääalgoritmi toimii rekursiolla, jajokaisella rekursiotasolla kutsut ovat toteutettujen tietorakenteiden ansiosta vakioaikaisia, joten saamme aikavaativuuden ylärajan seuraavasti: Olkoon `F` on joukko, jonka alkiot ovat joukkoja ja `F`:n alkioista voidaan rakentaa täsmällinen peite. Valitaan jokin `x` ja määritellään, että `C` on kaikkien niiden `F`:n alkioiden `S_i` joukko, joissa `x \in S_i`. Nyt algoritmi suorittaa `|C|` rekursiokutsua, joista jokaisella `F`:n koko on enimmillään `n - |C|`. Tästä saadaan ylärajaksi `O(3^(n/3)`.

Tilavaativuuden yläraja on `O(n)`, sillä linkitetyistä listoista koostettuun matriisiin tallennetaan ainostaan annettujen joukkojen elementtien kuvaus. Jokaista erillistä elementtiä kohtaan luodaan yksi kolumnisolmua ja jokaista elementtiä kohtaan luodaan yksi datasolmu. Esimerkiksi joukon `((1,2,4), (2,3,4))` kuvaamiseksi tarvitaan kuusi datasolmua sekä neljä kolumnisolmua.

# Suorituskyky ja O-analyysivertailu

Tulossa myöhemmin


# Työn mahdolliset puutteet ja parannusehdotukset

Tulossa myöhemmin

# Lähteet
- https://www.ocf.berkeley.edu/~jchu/publicportal/sudoku/0011047.pdf
- https://11011110.github.io/blog/2008/01/10/analyzing-algorithm-x.html
- https://en.wikipedia.org/wiki/Exact_cover
- https://en.wikipedia.org/wiki/Knuth%27s_Algorithm_X
- https://en.wikipedia.org/wiki/Dancing_Links
- https://en.wikipedia.org/wiki/Pentomino
- http://www.tcs.hut.fi/Studies/T-79.5202/2006SPR/slideswww.pdf (suomenkielistä terminologiaa)
- https://boyetblog.s3.amazonaws.com/PCPlus/294.pentominoes.pdf
