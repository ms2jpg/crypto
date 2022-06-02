# Wykorzystywanie algorytmu RSA do podpisu cyfrowego
Opis realizacji zadań dla wersji bez sumy kontrolnej.
1. Przygotowano wiadomość tekstową składającą się z 20-tu znaków.
2. Wygenerowano dwie pary kluczy: klucz publiczny oraz klucz prywatny. Para kluczy osoby A i osoby B.
3. Udostępniono klucze publiczne.
4. Podpisano wiadomość kluczami prywatnymi A i B (niezależnie).
5. Zweryfikowano podpis kluczami publicznymi A i B (niezależnie).
6. Sprawdzono zgodność między odszyfrowanymi plikami.

## Otrzymane dane
Sumy kontrolne odszyfrowanych wiadomości:
```
a58286345e9e94757f02af815478c22d  message_a.txt
a58286345e9e94757f02af815478c22d  message_b.txt
a58286345e9e94757f02af815478c22d  message.txt
```

## Wnioski
* Przy pomocy kryptografii asymetrycznej znając klucz publiczny osoby X jesteśmy w stanie stwierdzić, że dane pochodzą od osoby X poprzez odszyfrowanie kluczem publicznym (któremu ufamy) wiadomości lub sumy kontrolnej pliku.
* Klucze prywatne i publiczne można zastosować zamiennie zarówno do szyfrowania i deszyfrowania.

