Tuntimäärä: 15h

# Mitä olen tehnyt tällä viikolla?

Parantelin GUIta: lisäsin pentomino-ratkaisuiden näyttämisen käyttäjälle. Krijoitin hajautustaulupohjaisen version algoritmista, jotta toteutuksia voi vertailla. Kirjoitin lisäksi paljon testejä ja ohjelman testikattavuus on nyt kauttaaltaan hyvällä tasolla. Korjasin myös pentominoihin liittyvän suorituskykyä haitaneen bugin: aluksi ratkaisuja generoitiin liikaa, josta sitten karsittiin peilikuvat / käännöt pois. Nyt ohjelma generoi suoraan kaikki uniikit ratkaisut.

# Miten ohjelma on edistynyt?

Ohjelman on edistynyt oikein hyvin, rakennetta on selkeytetty entisestään, gui on parantunut ja ongelmia algoritmien toimivuuden kanssa ei ole. Ohjelmaa on helppo laajentaa tässä pari viimeistä viikkoa.

# Mitä opin tällä viikolla?

En kauheasti uutta. Opiskelin testaamiseen liittyen vähän python-spesifejä juttuja, joiden avulla testejä voidaan ajaa parametrisoidusti. Tämä vähentää melkoisesti boilerplaten määrää koodissa. Pentominojen ratkaisujen löytämistä nopeuttavien keinojen huomaaminen oli kiva homma.

# Mikä jäi epäselväksi tai tuottanut vaikeuksia?

Kun nyt tässä pythonin puolella ei tosiaan kannata kirjoittaa omia tietorakenteita (hajautustauluja, listoja jne.) valmiiden toteutusten tilalle, niin mietin, että kuinka paljon valmista tavaraa projektiin uskaltaa jättää. Koetanko karsia kuitenkin erilaiset valmiiden tietorakenteiden apumetodit (esim. reversed(list), kääntää listan) pois?

Lisäksi kyselisin, onko ohjelmassani tarpeeksi sisältöä, vaikka noita pythonin valmiita en toteuttaisikaan itse? Ajatuksena oli tehdä vikana hommana vielä sudokujen ratkaisuun sopiva laajennus.

# Mitä teen seuraavaksi?
- Sudokujen ratkaisemisen tuominen mukaan ohjelmaan
- dokumentointia, suorituskykymittauksia
