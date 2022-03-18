# 1. Testy szybkości

|Plik| Rozmiar  |
|---|:--------:|
|texts/pan-tadeusz-x1.txt|   492K   |
|texts/pan-tadeusz-x20.txt|   9,5M   |
|texts/pan-tadeusz-x200.txt|   95M    |
|texts/pan-tadeusz-x2000.txt|   942M   |

![benchmarks.png](benchmarks.png)
Czas szyfrowania plików jest liniowy. CFB jest o wyraźnie wolniejszy niż pozostałe tryby blokowe, które posiadają podobną charakterystykę.

# Anomalie
## AES-EBC
### Usunąć cały blok
```bash
./diff.sh raw/alphabet.bin decrypted/alphabet-aes-ecb_delete_block.bin
```
```diff
6162 6364 6566 6768 696a 6b6c 6d6e 6f70 abcdefghijklmnop        6162 6364 6566 6768 696a 6b6c 6d6e 6f70 abcdefghijklmnop
7172 7374 7576 7778 797a 6162 6364 6566 qrstuvwxyzabcdef        7172 7374 7576 7778 797a 6162 6364 6566 qrstuvwxyzabcdef
6768 696a 6b6c 6d6e 6f70 7172 7374 7576 ghijklmnopqrstuv     <
7778 797a 6162 6364 6566 6768 696a 6b6c wxyzabcdefghijkl        7778 797a 6162 6364 6566 6768 696a 6b6c wxyzabcdefghijkl
6d6e 6f70 7172 7374 7576 7778 797a 6162 mnopqrstuvwxyzab        6d6e 6f70 7172 7374 7576 7778 797a 6162 mnopqrstuvwxyzab
```
