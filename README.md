# Algorytmy i struktury danych – wyszukiwanie wzorca

## Implementacja algorytmów wyszukiwania wzorca

Napisane zostały trzy funkcje, które implementują następujące algorytmy wyszukiwania wzorca w tekście:

* algorytm N (tzw. naiwny),

* algorytm KMP (Knutha-Morrisa-Pratta),

* algorytm KR (Karpa-Rabina).

Kod implementacji algorytmów znajduje się w pliku `search.py`.

## Sprawdzenie poprawności implementacji

Przetestowane zostały wszystkie funkcje dla przypadków brzegowych dla różnych długości wzorca oraz tekstu. Dane testy oraz dodatkowe znajdują się w pliku `test_search.py`.
Wyniki testów oraz benchmarku znajdują się w `benchmark_test.png` oraz `test_result.png`.

## Porównanie algorytmów wyszukiwania wzorca

Jako tekst przeszukiwany wykorzystano plik `pan-tadeusz.txt`. Dla każdej z funkcji zmierzono czas wyszukiwania w całym pliku *n* pierwszych słów wczytanych z pliku (np. *n* = 100, 200, ..., 1000).

Także narysowano wspólny wykres dla wszystkich funkcji pokazujący zależność czasu wyszukiwania od liczby szukanych słów.

Porównanie algorytmów pod względem czasu wyszukiwania oraz generowanie wykresu znajduje się w pliku `times_test.py`.
Zdjęcia wykresów znajdują się w `times_plot.png`. 
