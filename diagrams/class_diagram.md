# Diagram Klas - The Temple of The Nameless Goddess

## Diagram w notacji Mermaid

```mermaid
classDiagram
    %% ========== FACTORY PATTERN ==========
    class Enemy {
        <<abstract>>
        -enemy_name: str
        -enemy_max_hp: int
        -enemy_damage_die: int
        -enemy_current_hp: int
        +__init__(name, max_hp, damage_die)
        +is_alive() bool
        +base_attack() int
        +take_damage(damage: int) void
        +__str__() str
    }

    class Rat {
        +__init__()
    }

    class Skeleton {
        +__init__()
        +base_attack() int
    }

    class Zombie {
        +__init__()
        +base_attack() int
    }

    class EnemyFactory {
        <<Factory Pattern>>
        +ENEMY_CLASS_MAPPING: dict
        +create_enemy()$ Enemy
    }

    class EnemyType {
        <<enumeration>>
        RAT
        ZOMBIE
        SKELETON
    }

    Enemy <|-- Rat : inherits
    Enemy <|-- Skeleton : inherits
    Enemy <|-- Zombie : inherits
    EnemyFactory ..> Enemy : creates
    EnemyFactory ..> EnemyType : uses
    EnemyFactory ..> Rat : creates
    EnemyFactory ..> Skeleton : creates
    EnemyFactory ..> Zombie : creates

    %% ========== STRATEGY PATTERN ==========
    class AttackOutcome {
        <<abstract>>
        +calculate_damage(base_damage: int)* int
    }

    class MissStrategy {
        +calculate_damage(base_damage: int) int
    }

    class GlancingBlowStrategy {
        +calculate_damage(base_damage: int) int
    }

    class FullHitStrategy {
        +calculate_damage(base_damage: int) int
    }

    class CritStrategy {
        +calculate_damage(base_damage: int) int
    }

    class AttackResolver {
        +map_combat_strategy(roll: int)$ AttackOutcome
    }

    class CombatStrategy {
        <<Strategy Pattern>>
        -combat_strategy: AttackOutcome
        +__init__()
        +define_strategy() void
        +attack(base_damage: int) int
    }

    AttackOutcome <|-- MissStrategy : implements
    AttackOutcome <|-- GlancingBlowStrategy : implements
    AttackOutcome <|-- FullHitStrategy : implements
    AttackOutcome <|-- CritStrategy : implements
    CombatStrategy o-- AttackOutcome : uses
    AttackResolver ..> AttackOutcome : creates
    CombatStrategy ..> AttackResolver : uses

    %% ========== CORE CLASSES ==========
    class Game {
        -player: Player
        -is_game_running: bool
        -nr_of_chambers: int
        +__init__(player_name: str)
        +start() void
        +combat(player, enemy)$ void
        +enter_room()$ tuple
    }

    class Player {
        -max_hp: int
        -player_name: str
        -current_hp: int
        -player_armor: int
        -player_weapon: int
        +__init__(player_name: str)
        +roll_equipment() void
        +is_alive() bool
        +take_damage(damage: int) void
        +base_attack() int
    }

    class SingleDie {
        +roll(die_type: int)$ int
        +roll_2d6()$ int
    }

    class Equipment {
        <<dataclass>>
        +equipment_type: EquipmentType
        +die: int
        +description: str
    }

    class EquipmentType {
        <<enumeration>>
        WEAPON
        ARMOR
        OTHER
    }

    class RoomType {
        <<enumeration>>
        ENEMY
        BOOK
        EMPTY
    }

    Game *-- Player : contains
    Game ..> Enemy : uses
    Game ..> CombatStrategy : uses
    Game ..> RoomType : uses
    Game ..> EnemyFactory : uses
    Player ..> SingleDie : uses
    Player ..> Equipment : uses
    Player ..> EquipmentType : uses
    Enemy ..> SingleDie : uses
    CombatStrategy ..> SingleDie : uses
    Equipment ..> EquipmentType : uses

    %% Styling
    style EnemyFactory fill:#ffeb99
    style CombatStrategy fill:#ffeb99
    style Enemy fill:#99ccff
    style AttackOutcome fill:#99ccff
```

## Legenda

### Wzorce projektowe:
- **Factory Pattern** (żółty) - `EnemyFactory` do tworzenia wrogów
- **Strategy Pattern** (żółty) - `CombatStrategy` do obliczania obrażeń

### Typy klas:
- **Klasy abstrakcyjne** (niebieski) - `Enemy`, `AttackOutcome`
- **Klasy konkretne** (biały) - implementacje wzorców
- **Enumeracje** - `EnemyType`, `RoomType`, `EquipmentType`
- **Dataclass** - `Equipment`

### Relacje:
- **Dziedziczenie** (△──) - Rat, Skeleton, Zombie dziedziczą po Enemy
- **Kompozycja** (◆──) - Game zawiera Player
- **Agregacja** (◇──) - CombatStrategy używa AttackOutcome
- **Zależność** (╌╌>) - klasa używa innej klasy

## Opis wzorców

### 1. Factory Pattern (`EnemyFactory`)
**Cel:** Centralizacja tworzenia obiektów wrogów.

**Implementacja:**
- Klasa bazowa `Enemy` (abstrakcyjna)
- Konkretne implementacje: `Rat`, `Skeleton`, `Zombie`
- Fabryka `EnemyFactory` z metodą `create_enemy()`
- Mapowanie typów przez słownik `ENEMY_CLASS_MAPPING`

**Zalety:**
- Łatwe dodawanie nowych typów wrogów
- Spójność tworzenia obiektów
- Oddzielenie logiki tworzenia od logiki gry

### 2. Strategy Pattern (`AttackOutcome`)
**Cel:** Dynamiczne wybieranie algorytmu obliczania obrażeń.

**Implementacja:**
- Interfejs `AttackOutcome` (abstrakcyjna klasa bazowa)
- Konkretne strategie: `MissStrategy`, `GlancingBlowStrategy`, `FullHitStrategy`, `CritStrategy`
- Kontekst `CombatStrategy` przechowujący wybraną strategię
- Resolver `AttackResolver` mapujący rzut kości na strategię

**Zalety:**
- Brak wielokrotnych instrukcji warunkowych
- Łatwe dodawanie nowych typów ataków
- Kod zgodny z zasadą Open/Closed (otwarty na rozszerzenia, zamknięty na modyfikacje)

## Przepływ danych

1. **Inicjalizacja gry:**
   ```
   main() → Game(player_name) → Player(player_name) → roll_equipment()
   ```

2. **Wejście do pokoju:**
   ```
   Game.enter_room() → SingleDie.roll(6) → ROOM_TABLE → RoomType
   ```

3. **Tworzenie wroga (Factory Pattern):**
   ```
   EnemyFactory.create_enemy() → roll(6) → ENEMY_TABLE → EnemyType
   → ENEMY_CLASS_MAPPING[type]() → Rat/Skeleton/Zombie
   ```

4. **Walka (Strategy Pattern):**
   ```
   CombatStrategy.define_strategy() → roll_2d6() → AttackResolver
   → map_combat_strategy(roll) → MissStrategy/GlancingBlowStrategy/etc.
   → attack(base_damage) → combat_strategy.calculate_damage()
   ```
