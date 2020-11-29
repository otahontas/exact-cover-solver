# Testausdokumentti

## Testien rakenne

Yksikkötesteissä testataan ohjelman toimivuutta melko pienillä, mutta silti eri tyyppisillä syötteille. Syötteet tarjotaan enimmäkseen muodossa, jossa on jokin universumi (esim. luvut 1-7) sekä joukko universumin elementeistä koostuvia joukkoja. 

Suorituskykytestit testaavat isoissa hakuavaruuksissa tapahtuvaa laskentaa:
- erityyppisten pentomino-lautojen (3x20, 4x15, 5x12, 6x10) vastausten lukumäärät
- harvaan täytettyjen sudokujen vastausten lukumäärät

Testeillä saadaan eroteltua kahden algoritmin toimivuutta:
- raportti seuraa myöh...

## Testien ajaminen 

Testit voi ajaa yksinkertaisesti komennolla `pypy3 performance_tests/main.py`. Pypyn käyttö on tässä vahvasti suositeltavaa. Ohjelma ajaa algoritmien toteutukset eri tyyppisiä ongelmia vastaan ja raportoi tulokset.

## Graafeja tms.

## Pentomino-ongelmat
|Algoritmi   	| Laudan koko | Hakuavaruuden koko  | Ratkaisuita | Kesto (sek) |
|---	        |---	        |---	                |             |             |
| DLX	        | 3x20	      |---	                |  2          | 0.52	      |
| DLX	        | 4x15	      |---	                |  368        | 5.21        |
| DLX	        | 5x12	      |---	                |  1010       | 12.7	      |
| DLX	        | 6x10        |---	                |  2339       | 22.8        |
| DictX	      | 3x20	      |---	                |  2     	    | 1.2   	    |
| DictX       | 4x15	      |---	                |  368   	    | 16.67	      |
| DictX       | 5x12	      |---	                |  1010  	    | 40.9	      |
| DictX	      | 6x10	      |---	                |  2339  	    | 77.15	      |
