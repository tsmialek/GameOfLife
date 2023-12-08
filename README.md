# GameOfLife
Classic Game Of Life implementation in python

## Użyte wzorce:
- Factory: ButtonFactory i CellFactory *(Cell Factory jest tu zaimplementowane bardzo na siłe moim zdaniem)*
  ButtonFactory implementuje poszczególne klasy rodzajów przycisków:
  - SaveButton, LoadButton, NextGenerationButton, ExitButton, AutomaticGenButton oraz PauseButton
    W klaasach przycisków jest odrazu zaimplementowana logika specyficzna dla każdego z nich
    W klase z Button z której dziedziczą wszystkie przyciski zaimplementowana została logika wspólna dla każdego przycisku *(metoda draw() oraz click_detection())*
    ButtonFactory zwraca dany typ przycisku na podstawie podanego parametru. *(jest to krótsza implementacja wzorca factory który nie uwzględnia specyficznych fabryk)*
  CellFactory implementuje klasy komórek:
  - AliveCell i DeadCell dziedziczące po klasie Cell. Moim zdaniem zastosowanie tego wzorca tutaj jest niepraktyczne ponieważ
    istnieją tylko 2 rodzaje komórek, oraz różnią się one tylko kolorem. Zaimplementowałem ten wzorzec jedynie w celach treningowych.
    AliveCell i DeadCell posiadają metode draw() która umożliwia narysowanie komórki na ekranie
    CellFactory w metodzie create_cell() na podstawie podanego typu komórki zwraca odpowiadający specyficzny obiekt. *(jest to krótsza implementacja wzorca factory który nie uwzględnia specyficznych fabryk)*

- Singleton: PygameSingleton jest klasą przechowującą wszystkie parametry gry i udostępniającą metody do uzyskiwania tych parametrów.
  Klasa ta jest też odpowiedzialna za inicjalizowanie modułu pygame oraz screen setup.
---
## Zapisywanie i wczytywanie
Zapisywanie i wczytywanie odbywa się poprzez zapisanie stanu tablicy game_state do pliku txt gdzie 1 oznaczają żywe a 0 martwe komórki.
Przy wczytywaniu plik txt zostaje zamieniony spowrotem na tablicę. 
Logikę zapisywania i wczytywania obsługują metody click_logic razem z metodami pomocniczymi znajdującymi się 
odpowiednio w klasach SaveButton i LoadButton w pliku ButtonFactory.py

## Automatyczne generowanie komórek
Automatyczne generowanie komórek działa dokładnie tak samo jak manualne generowanie komórek, 
tylko jest wykonywane w pętli po upływie ustalonej liczby sekund. 
