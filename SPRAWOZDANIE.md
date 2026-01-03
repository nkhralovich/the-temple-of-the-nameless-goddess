# Sprawozdanie - Wzorce Projektowe
## The Temple of The Nameless Goddess

**Autor:** [Twoje imię i nazwisko]
**Data:** 2026-01-03
**Temat:** Implementacja wzorców projektowych w grze RPG

---

## 1. Omówienie programu

### 1.1 Dziedzina problemowa
Program implementuje tekstową grę RPG w stylu dungeon crawler. Gracz wciela się w poszukiwacza przygód, który eksploruje krypty świątyni Bezimiennej Bogini w poszukiwaniu starożytnej księgi.

### 1.2 Mechanika gry
Gra oparta jest na mechanice znane z gier RPG:
- **Tworzenie postaci**: Losowanie HP (1d6) i ekwipunku (broń/zbroja)
- **Eksploracja**: Losowe generowanie pokoi (pusty/wróg/skarbiec)
- **System walki**: Oparty na rzutach kośćmi (2d6 dla trafienia, damage die dla obrażeń)
- **Wrogowie**: Różne typy wrogów z unikalnymi statystykami (Szczur, Szkielet, Zombie)
- **Warunek zwycięstwa**: Znalezienie księgi
- **Warunek przegranej**: Śmierć postaci (HP = 0)

### 1.3 Struktura kodu
```
the-temple-of-the-nameless-goddess/
├── main.py              # Punkt wejścia, główna pętla gry
├── game.py              # Logika gry
├── player.py            # Klasa gracza
├── enemy.py             # Hierarchia wrogów + Factory Pattern
├── combat.py            # System walki + Strategy Pattern (kontekst)
├── damage.py            # Strategy Pattern (strategie)
├── dice_roller.py       # System rzutów kośćmi
├── equipment.py         # System ekwipunku
└── room.py              # Typy pokoi
```

---

## 2. Zastosowane wzorce projektowe

### 2.1 Factory Pattern

#### Uzasadnienie zastosowania
W grze RPG występują różne typy wrogów o różnych statystykach (HP, obrażenia, zachowania). Factory Pattern pozwala na:
- **Centralne zarządzanie** tworzeniem wrogów
- **Łatwe dodawanie** nowych typów wrogów bez modyfikacji kodu gry
- **Spójność danych** - wszystkie wrogowie tworzone są przez jeden mechanizm
- **Losowe generowanie** - fabryka integruje się z systemem losowania

#### Implementacja
**Lokalizacja:** `enemy.py` (linie 95-114)

**Komponenty:**
1. **Produkt abstrakcyjny**: `Enemy` (klasa abstrakcyjna ABC)
2. **Produkty konkretne**: `Rat`, `Skeleton`, `Zombie`
3. **Fabryka**: `EnemyFactory` z metodą statyczną `create_enemy()`

**Kod:**
```python
class EnemyFactory:
    ENEMY_CLASS_MAPPING = {
        EnemyType.RAT: Rat,
        EnemyType.SKELETON: Skeleton,
        EnemyType.ZOMBIE: Zombie
    }

    @staticmethod
    def create_enemy() -> Enemy:
        roll = SingleDie.roll(die_type=6)
        enemy_type = ENEMY_TABLE[roll]
        enemy = EnemyFactory.ENEMY_CLASS_MAPPING.get(enemy_type)

        if enemy:
            return enemy()
        return None
```

**Zalety:**
- ✅ Dodanie nowego wroga wymaga tylko: (1) utworzenia klasy dziedziczącej po `Enemy`, (2) dodania wpisu do `ENEMY_CLASS_MAPPING`
- ✅ Główna logika gry nie wie, jak konkretnie tworzyć wrogów
- ✅ Łatwe testowanie - można mockować fabrykę

#### Diagram klas (Fragment - Factory Pattern)
```
        Enemy (ABC)
           ↑
    ┌──────┼──────┐
    │      │      │
   Rat  Skeleton Zombie
           ↑
           │
      EnemyFactory
      (creates)
```

---

### 2.2 Strategy Pattern

#### Uzasadnienie zastosowania
System walki wykorzystuje mechanikę attack roll (2d6), która może dać różne wyniki:
- **≤6**: Chybienie (0 obrażeń)
- **7-9**: Lekkie trafienie (połowa obrażeń)
- **10-11**: Pełne trafienie (pełne obrażenia)
- **12**: Trafienie krytyczne (podwojone obrażenia)

Strategy Pattern pozwala:
- **Elegancko obsłużyć** każdy typ wyniku bez używania wielokrotnych `if-elif-else`
- **Łatwo rozszerzać** system o nowe typy ataków (np. trucizna, ogień)
- **Zachować zasadę Open/Closed** - otwarty na rozszerzenia, zamknięty na modyfikacje

#### Implementacja
**Lokalizacja:** `damage.py` (strategie), `combat.py` (kontekst)

**Komponenty:**
1. **Strategia abstrakcyjna**: `AttackOutcome` (ABC)
2. **Strategie konkretne**: `MissStrategy`, `GlancingBlowStrategy`, `FullHitStrategy`, `CritStrategy`
3. **Kontekst**: `CombatStrategy`
4. **Resolver**: `AttackResolver` (mapuje rzut na strategię)

**Kod strategii:**
```python
class AttackOutcome(ABC):
    @abstractmethod
    def calculate_damage(self, base_damage: int) -> int:
        pass

class MissStrategy(AttackOutcome):
    def calculate_damage(self, base_damage: int) -> int:
        return 0

class GlancingBlowStrategy(AttackOutcome):
    def calculate_damage(self, base_damage: int) -> int:
        return base_damage // 2

class FullHitStrategy(AttackOutcome):
    def calculate_damage(self, base_damage: int) -> int:
        return base_damage

class CritStrategy(AttackOutcome):
    def calculate_damage(self, base_damage: int) -> int:
        return base_damage * 2
```

**Kod kontekstu:**
```python
class CombatStrategy:
    def __init__(self):
        self.combat_strategy = None

    def define_strategy(self):
        strategy_roll = SingleDie.roll_2d6()
        self.combat_strategy = AttackResolver.map_combat_strategy(strategy_roll)

    def attack(self, base_damage):
        final_damage = self.combat_strategy.calculate_damage(base_damage)
        return final_damage
```

**Zalety:**
- ✅ Brak długich łańcuchów `if-elif-else` w kodzie walki
- ✅ Każda strategia jest niezależną klasą - łatwe testowanie
- ✅ Dodanie nowego typu trafienia to tylko nowa klasa implementująca `AttackOutcome`
- ✅ Kod zgodny z Single Responsibility Principle

#### Diagram klas (Fragment - Strategy Pattern)
```
    AttackOutcome (ABC)
           ↑
    ┌──────┼──────┬─────────┐
    │      │      │         │
   Miss Glancing Full     Crit
         Blow    Hit
           ↑
           │ uses
    CombatStrategy
    (context)
```

---

## 3. Diagramy

### 3.1 Diagram klas
Zobacz plik: `class_diagram.md`

Diagram pokazuje:
- Pełną hierarchię klas projektu
- Relacje między klasami (dziedziczenie, kompozycja, agregacja, zależność)
- Wzorce projektowe oznaczone kolorem żółtym
- Klasy abstrakcyjne oznaczone kolorem niebieskim

### 3.2 Diagram sekwencji
Zobacz plik: `sequence_diagram.md`

Diagramy pokazują:
1. **Tworzenie wroga** - przepływ Factory Pattern
2. **Walka** - przepływ Strategy Pattern (jedna runda)
3. **Pełny przebieg gry** - od inicjalizacji do końca

---

## 4. Przebieg gry - przykład

```
=== Welcome to The Temple of The Nameless Goddess ===
Hello, brave adventurer! Name yourself: Alice
Welcome, Alice! Your goal: get the artifact placed in the Main Crypt Chamber...

Your starting equipment is a sword. Congrats!
Player created! HP: 4, armor: 0, weapon die: d6

You enter a room...
You see rows of sealed stone coffins. Something moves in the shadows...
Your eyes are adjusted to darkness and you see a Shaky old skeleton!
The enemy tries to attack, but you have better reaction and attack first.
Enemy takes 3 damage.
You won!

You enter a room...
Nothing here. Moving to the next room.

You enter a room...
You see a big room, moss on the walls, heavy air, and an ancient altar...
Come get your book, you lucky bastard! And get out of here.
```

---

## 5. Możliwości rozszerzenia

Dzięki zastosowanym wzorcom projektowym, łatwo można:

### Nowe typy wrogów (Factory Pattern)
```python
class Dragon(Enemy):
    def __init__(self):
        super().__init__(
            enemy_name="Ancient Dragon",
            enemy_max_hp=20,
            enemy_damage_die=12
        )
```

### Nowe strategie ataku (Strategy Pattern)
```python
class PoisonStrategy(AttackOutcome):
    def calculate_damage(self, base_damage: int) -> int:
        # Trucizna: normalne obrażenia + 2 przez 3 tury
        return base_damage + 2
```

---

## 6. Narzędzia i technologie

- **Język programowania**: Python 3.x
- **Biblioteki standardowe**: `random`, `abc`, `enum`, `dataclasses`
- **Narzędzia**: Git, VSCode/PyCharm
- **Wzorce projektowe**: Factory Pattern, Strategy Pattern

---

## 7. Wnioski

### 7.1 Factory Pattern
✅ **Zalety:**
- Łatwe dodawanie nowych wrogów bez modyfikacji głównej logiki gry
- Centralizacja tworzenia obiektów
- Lepsze testowanie (mockowanie fabryki)

⚠️ **Potencjalne wady:**
- Dodatkowa warstwa abstrakcji (ale w tym przypadku uzasadniona)

### 7.2 Strategy Pattern
✅ **Zalety:**
- Brak skomplikowanych instrukcji warunkowych
- Łatwe rozszerzanie systemu walki
- Kod zgodny z SOLID principles
- Każda strategia testowalna osobno

⚠️ **Potencjalne wady:**
- Więcej klas (ale każda jest prosta i ma jedno zadanie)

### 7.3 Podsumowanie
Zastosowanie wzorców projektowych sprawiło, że kod jest:
- **Łatwiejszy do utrzymania** - zmiana zachowania wymaga edycji tylko jednej klasy
- **Skalowalny** - dodawanie nowych funkcji nie wymaga modyfikacji istniejącego kodu
- **Czytelny** - każda klasa ma jasno określoną odpowiedzialność
- **Testowalny** - małe, niezależne jednostki łatwo testować

---

## 8. Bibliografia

1. Gamma, E., Helm, R., Johnson, R., Vlissides, J. (1994). *Design Patterns: Elements of Reusable Object-Oriented Software*. Addison-Wesley.
2. Refactoring Guru - Design Patterns: https://refactoring.guru/design-patterns
3. Python Documentation: https://docs.python.org/3/
4. Real Python - Object-Oriented Programming: https://realpython.com/python3-object-oriented-programming/

---

## Załączniki

1. `class_diagram.md` - Diagram klas w notacji Mermaid
2. `sequence_diagram.md` - Diagramy sekwencji w notacji Mermaid
3. Kod źródłowy w repozytorium Git

---

**Koniec sprawozdania**
