# Szyfr cezara z dowolnym przestawieniem
Rodzaj szyfru podstawieniowego, w którym każda litera tekstu jawnego oddalonego o stałą liczbę pozycji w alfabecie. Szyfr nie jest bezpieczny z uwagi na bardzo proste zastosowanie technik bruteforce.

## Przykład
Przykład alfabetu i szyfru dla przesunięcia równego 3:
```
Alfabet: AĄBCĆDEĘFGHIJKLŁMNŃOÓPRSŚTUWYZŹŻ
  Szyfr: CĆDEĘFGHIJKLŁMNŃOÓPRSŚTUWYZŹŻAĄB
```
i przykład zaszyfrowania:
```
Tekst jawny: MĘŻNY BĄDŹ, CHROŃ PUŁK TWÓJ I SZEŚĆ FLAG
Tekst zaszyfrowany: OHBÓŻ DĆFĄ, EKTRP ŚZŃM YŹSŁ L UAGWĘ INCJ
```
## Alfabet
Alfabet zależnie od konfiguracji programu może się składać z:
* mały i wielkich liter alfabetu
* cyfr
* polskich znaków

Znaki białe oraz interpunkcyjne są przepisywane bez zmian.

## Dane wejściowe
Dowolny tekst o dowolnym rozmiarze wpisany z klawiatury lub załadowany z pliku.

## Uruchomienie
Wymagany python 3.7+:
```
python3 main.py
```

# Szyfr Provenzano
[Źródło](http://itre.cis.upenn.edu/~myl/languagelog/archives/003049.html)
Szyfr wykorzystywany przez włoskiego mafiozę Bernardo Provenzano. Ta wersja polegała na wykorzystaniu szyfru cezara z przesunięciem równym 3 oraz zapisaniu liczby porządkowej litery zamiast samej litery (a -> 1, b -> 2).

|Kod|Litera|
|---|---|
| 4 |	a |
| 5 |	b |
| 6 |	c |
| 7 |	d |
| 8 |	e |
| 9 |	f |
| 10 |	g |
| 11 |	h |
| 12 |	i |
| 13 |	l |
| 14 |	m |
| 15 |	n |
| 16 |	o |
| 17 |	p |
| 18 |	q |
| 19 |	r |
| 20 |	s |
| 21 |	t |
| 22 |	u |
| 23 |	v |
| 24 |	z |

Szyfr nie zawiera wszystkich 25 liter znanego nam alfabetu z uwagi na specyfikę alfabetu włoskiego.

## Przykład
```
10 12 23 4 15 15 12	14 8 19 6 4 7 4 15 21 8
 g  i v  a  n  n  i	 m e  r c a d a  n  t e
 ```
