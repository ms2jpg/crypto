# Kryptografia wizualna
## Założenia
Dane wejściowe:
* obraz JPG/BMP/PNG czarno biały bez przezroczystości, brak ograniczeń co do wielkości obrazu.

Dane wyjściowe:
* dwa obrazki PNG o takiej samej wysokosci jak obrazek źródłowy, lecz z dwukrotnie większą szerokością.

## Opis algorytmu
Algorytm wykorzystuje poniższą matrycę przekształceń do tworzenia obrazów wynikowych. Dla każdej wartości w obrazie źródłowym występują dwie możliwości w obrazach wynikowych. Prawdopodobieństwo wystąpienia każdej możliwości jest jednakowe.

| Obraz źródłowy | Obraz wynikowy 1 | Obraz wynikowy 2 |
|:--------------:|:----------------:|:----------------:|
|       0        |        10        |        10        |
|       0        |        01        |        01        |
|       1        |        10        |        01        |
|       1        |        01        |        10        |

W wyniku odpowiedniego doboru parametrów trasformacji funkcja powrotna zwraca biały kolor dla równych par grup pixeli i czarny dla różnych.

## Środowisko uruchomieniowe
Jupyter z kernelem Python, najprościej uruchomić kontener [jupyter/minimal-notebook](https://hub.docker.com/r/jupyter/minimal-notebook) lub Python 3.x z bibliotekami numpy, pillow, matplotlib.

## Testy
Przy nałożeniu dwóch fragmentów w GIMP przy ustawieniu krycie = 50% dla górnej warstwy widać wyraźnie wzór oryginalny. Oryginalny czarny kolor na połączonych warstwach jest szary, a biały oryginalny kolor jest czarny lub biały.
![gimp.png](https://i.imgur.com/hGa3tsu.png)
Sprawdzone zostały również różne tryby krycia w GIMP przy kryciu 100%:

|          Tryb          |                                        Wynik                                         |
|:----------------------:|:------------------------------------------------------------------------------------:|
|         Zwykłe         |                                      Brak zmian                                      |
|      Przenikanie       |                                      Brak zmian                                      |
|  Tryb usuwania koloru  | Czarny oryginalny kolor jest czarno biały, biały oryginalny kolor jest przezroczysty |
|       Wycieranie       |                            Obraz jest cały przezroczysty                             |
|        Łączenie        |                                Obraz jest cały szary                                 |
|       Dzielenie        |                            Obraz jest cały przezroczysty                             |
|    Tylko jaśniejsze    |              Oryginalny czarny jest biały, oryginalny biały jest szary               |
| Tylko jaśniejsze lumy  |              Oryginalny czarny jest biały, oryginalny biały jest szary               |
|      Przesiewanie      |              Oryginalny czarny jest biały, oryginalny biały jest szary               |
|      Rozjaśnianie      |                                Obraz jest cały szary                                 |
|          Suma          |              Oryginalny czarny jest biały, oryginalny biały jest szary               |
|   Tylko ciemniejsze    |              Oryginalny czarny jest czarny, oryginalny biały jest szary              |
| Tylko ciemniejsze lumy |              Oryginalny czarny jest czarny, oryginalny biały jest szary              |
|        Mnożenie        |              Oryginalny czarny jest czarny, oryginalny biały jest szary              |
|     Przyciemianie      |                                Cały obraz jest szary                                 |
| Liniowe przyciemnianie |              Oryginalny czarny jest czarny, oryginalny biały jest szary              |
|       Pokrywanie       |                                Cały obraz jest szary                                 |
|    Miękkie światło     |                                Cały obraz jest szary                                 |
|     Twarde światło     |                                Cały obraz jest szary                                 |
|      Żywe światło      |                                Cały obraz jest szary                                 |
|    Światło punktowe    |                                Cały obraz jest szary                                 |
|    Światło liniowe     |                                Cały obraz jest szary                                 |
|    Twarda mieszanka    |              Oryginalny czarny jest biały, oryginalny biały jest szary               |
|        Różnica         |                       Oryginalny obraz z odwróconymi kolorami                        |
|      Wykluczenie       |                       Oryginalny obraz z odwróconymi kolorami                        |
|      Odejmowanie       |              Oryginalne czarne jest szare, Oryginalne białe jest czarne              |

## Wnioski
Kryptografia wizualna może być użyteczna do przekazania wiadomości w pozornie nic nie znaczących strumeiniach bajtów/szumach/szarościach. Wykorzystanie dwóch części wiadomości pozwala na wysłanie ich dwoma niezależnymi kanałami nieznanymi lub częściowo nieznanymi dla napastnika.
