# Badanie funkcji skrótu
## Badanie skrótów pliku oryginalnego i zmodyfikowanego
Plik oryginalny
```
LOREMIPSUMISSIMPLYDUMMYTEXTOFTHEPRINTINGANDTYPESETTINGINDUSTRYLOREMIPSUMHASBEENTHEINDUSTRYSSTANDARDDUMMYTEXTEVERSINCETHESWHENANUNKNOWNPRINTERTOOKAGALLEYOFTYPEANDSCRAMBLEDITTOMAKEATYPESPECIMENBOOKITHASSURVIVEDNOTONLYFIVECENTURIESBUTALSOTHELEAPINTOELECTRONICTYPESETTINGREMAININGESSENTIALLYUNCHANGEDITWASPOPULARISEDINTHESWITHTHERELEASEOFLETRASETSHEETSCONTAININGLOREMIPSUMPASSAGESANDMORERECENTLYWITHDESKTOPPUBLISHINGSOFTWARELIKEALDUSPAGEMAKERINCLUDINGVERSIONSOFLOREMIPSUM
```
Zmodyfikowany plik
```
JOREMIPSUMISSIMPLYDUMMYTEXTOFTHEPRINTINGANDTYPESETTINGINDUSTRYLOREMIPSUMHASBEENTHEINDUSTRYSSTANDARDDUMMYTEXTEVERSINCETHESWHENANUNKNOWNPRINTERTOOKAGALLEYOFTYPEANDSCRAMBLEDITTOMAKEATYPESPECIMENBOOKITHASSURVIVEDNOTONLYFIVECENTURIESBUTALSOTHELEAPINTOELECTRONICTYPESETTINGREMAININGESSENTIALLYUNCHANGEDITWASPOPULARISEDINTHESWITHTHERELEASEOFLETRASETSHEETSCONTAININGLOREMIPSUMPASSAGESANDMORERECENTLYWITHDESKTOPPUBLISHINGSOFTWARELIKEALDUSPAGEMAKERINCLUDINGVERSIONSOFLOREMIPSUM
```
### SHA-256
```
Oryginalny plik:
11011100100101011110010111101110011001011000110100001101001001001101001010101011111011100101010100111001111101010111111101111011101100010011001111110111001001010101100011110000100000111100010011000101111111111011101100100
Zmodyfikowany:
1001011110100111100111101011000010010001100010101110110101111111111011001110101011101111100010011101011000100011101000100000100100111011101101110101101010110101100110010101100011110010110001011001101110100101110001111011011101011
Diff:
1x01x1xx10xx01x11xxxx1xx1x1xxxx0xxxx0x0110001xxxxxx011010x1xx1xx11xxxxx01x10101x1110111xxx0xxx01xxx1xxxxxx1x0xx1xx1xxx1x0xxx10x1x011x0x1x0110x11x1x1xx1xx01x0101xx01100xx1x1x0001xxx001x1100010x1x0xxxx11x1xx1x11xxxxx11x01x0
```
Około 48.868778280542985% bitów zostało zmienionych w sumie kontrolnej po zmianie pliku źródłowego.

### SHA-512
```
Oryginalny plik:
1100001110000110110011110001011110100111100101100001011111001101110110111111110110111111101011010010101101100011101001011110010100001111000110111100011000111111010111110001001100010111110010011010110011010001100001110110101110000100011001100111010000101111010001001001101000111010111111110010001111001101000001011100110001011111111100011110110010000110111001111101110110001100111101001011101000001001100100100101100110110110100010101111111110010101011100000
Zmodyfikowany:
11000011000011111011011101101110101111101110101001101000011000101110111100111111010001010100011101111101001111000011110001001110011111101101101110001100101110001100110100110110010011111111001001100001101001111100110001101001101111101101010001110111111001001100100011011000011111100100000001011001101001010101100110110000100100101010000011100001000001111011110100101101110100110000111000001000000010011011100111111101000111010111
Diff:
11000011x000x11x1xxxx1110xxxx11x101xx11x1xxxxx100xxxxxxxx1x0xxxx11xx1x11xx1111x1xxxxx1x1xxx0x1x10x1x1xx10x1xxxxxx01xx10xx1x0x1xx0xxx111xxx0110111x00x1x0x0111xxxx10x11x100x10x1x0x0xx11111xxx0xxxx10xx0x1xxx0xx11x00x1xx011010x110xxx1x0x1xx01x0011101xxxx10x1xxx100xx001x0110x00x111x10x1xxxxxx0xxxx0x11xx0x1010x0xxx011xxxxx00xx01xx1x1x1x000x1110xx0xx000011x1x1xx1x1xxxx11011x0xxxxxxxxxx1x0x0xx10x00000100110x1x0xxx1x11x01x0x1x1xxxxxx
```
Około 49.065420560747663% bitów zostało zmienionych w sumie kontrolej po modyfikacji pliku źródłowego.

## Kolizje sum kontrolnych SHA-1
### Dla 16 bitów
Dwa pierwsze bajty sum kontrolnych SHA-1 są identyczne. 
```
1e6dccfacff2d4d67d94b30b04921e30fb4e2e02  printable-dangerous.txt
1e6d198933b24f1538febdb787597b97188ccb22  printable-harmless.txt
ea66f5a7faf9c86ef6a7944a6af1c0b4bd0a1e1c  unprintable-harmless.txt
ea662f54e5c580183af4194f9de9583463243dca  unprintable-dangerous.txt
```
Statystyki szukania kolizji dla wersji "printable":

| RunNo. | Steps until collision | Check of the collision | Total steps |
|:------:|:---------------------:|:----------------------:|:-----------:|
|   01   |          63           |           61           |     124     |
|   02   |          488          |          442           |     930     |
|   03   |          308          |          234           |     542     |
|   04   |          224          |          138           |     362     |
|   05   |          481          |          450           |     931     |

Statystyki szukania kolizji dla wersji "unprintable":

| RunNo. | Steps until collision | Check of the collision | Total steps |
|:------:|:---------------------:|:----------------------:|:-----------:|
|   01   |          198          |          106           |     304     |


### Dla 32 bitów
Cztery pierwsze bajty sum kontrolnych SHA-1 są identyczne.
```
b66a2f54e5c580183af4194f9de9583463243dca  printable-dangerous.txt
b66a2f54afbd2d8129aac00e7ba17fa7acefdbf1  printable-harmless.txt
62887d02fd8d96a9f88d930549272f7de91ef443  unprintable-dangerous.txt
62887d0228b7973dc96356ad157f3e6d76c07580  unprintable-harmless.txt
```

Statystyki szukania kolizji dla wersji "printable":

| RunNo. | Steps until collision | Check of the collision | Total steps |
|:------:|:---------------------:|:----------------------:|:-----------:|
|   01   |        51,072         |         44,504         |   95,576    |
 |   02   |        67,270         |         66,837         |   134,107   |

Statystyki szukania kolizji dla wersji "unprintable":

| RunNo. | Steps until collision | Check of the collision | Total steps |
|:------:|:---------------------:|:----------------------:|:-----------:|
|   01   |        106,560        |        106,549         |   213,109   |
|   02   |        58,288         |         57,504         |   115,792   |

# Cechy funkcji skrótu
* funkcja przyporządkowująca dowolnie dużej liczbie krótką wartość o stałym rozmiarze, tzw. skrót nieodwracalny
* słaba bezkolizyjność - dany jest skrót h(m) i odpowiadaj ąca mu wiadomość m. Znalezienie
wiadomości m’ ≠ m, takiej że h(m) = h(m’), jest obliczeniowo trudne.
* silna bezoklizyjność -obliczeniowo trudne jest znalezienie dowolnej pary różnych wiadomości m’ i m,
takich że h(m) = h(m’).

# Wnioski
Funkcje skrótu można zastosować do:
* weryfikacji integralności danych (np. pliku ISO systemu operacyjnego)
* podpisów cyfrowych
* przechowywanie haseł
* sygnatury wirusów
* generowanie ciagów pseudolosowych
* wykorzystanie w protokołach np. SSH, SSL