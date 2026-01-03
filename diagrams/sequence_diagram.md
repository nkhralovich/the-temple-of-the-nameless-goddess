# Diagramy Sekwencji - The Temple of The Nameless Goddess

## 1. Diagram sekwencji - Tworzenie wroga (Factory Pattern)

```mermaid
sequenceDiagram
    participant Main as main()
    participant Game as Game
    participant Factory as EnemyFactory
    participant Die as SingleDie
    participant Table as ENEMY_TABLE
    participant Enemy as Rat/Skeleton/Zombie

    Main->>Game: enter_room()
    Game->>Die: roll(die_type=6)
    Die-->>Game: room_roll (1-6)
    Game->>Table: ROOM_TABLE[room_roll]
    Table-->>Game: RoomType.ENEMY

    Note over Game,Factory: Factory Pattern w akcji
    Game->>Factory: create_enemy()
    Factory->>Die: roll(die_type=6)
    Die-->>Factory: enemy_roll (1-6)
    Factory->>Table: ENEMY_TABLE[enemy_roll]
    Table-->>Factory: EnemyType (RAT/SKELETON/ZOMBIE)
    Factory->>Factory: ENEMY_CLASS_MAPPING[enemy_type]
    Factory->>Enemy: __init__()
    Enemy-->>Factory: enemy instance
    Factory-->>Game: enemy
    Game-->>Main: (RoomType.ENEMY, enemy)
```

## 2. Diagram sekwencji - Walka (Strategy Pattern)

```mermaid
sequenceDiagram
    participant Main as main()
    participant Game as Game
    participant Player as Player
    participant CS as CombatStrategy
    participant Resolver as AttackResolver
    participant Die as SingleDie
    participant Strategy as AttackOutcome
    participant Enemy as Enemy

    Note over Main,Enemy: Runda walki - atak gracza
    Main->>Game: combat(player, enemy)

    Game->>Player: base_attack()
    Player->>Die: roll(player_weapon)
    Die-->>Player: base_damage
    Player-->>Game: base_damage

    Note over Game,Strategy: Strategy Pattern - wybór strategii ataku
    Game->>CS: CombatStrategy()
    CS-->>Game: combat_strategy
    Game->>CS: define_strategy()
    CS->>Die: roll_2d6()
    Die-->>CS: attack_roll (2-12)
    CS->>Resolver: map_combat_strategy(attack_roll)

    alt attack_roll == 12
        Resolver-->>CS: CritStrategy()
    else attack_roll >= 10
        Resolver-->>CS: FullHitStrategy()
    else attack_roll >= 7
        Resolver-->>CS: GlancingBlowStrategy()
    else attack_roll <= 6
        Resolver-->>CS: MissStrategy()
    end

    CS-->>Game: strategy assigned
    Game->>CS: attack(base_damage)
    CS->>Strategy: calculate_damage(base_damage)

    alt Miss
        Strategy-->>CS: 0
    else Glancing Blow
        Strategy-->>CS: base_damage // 2
    else Full Hit
        Strategy-->>CS: base_damage
    else Critical
        Strategy-->>CS: base_damage * 2
    end

    CS-->>Game: final_damage
    Game->>Enemy: take_damage(final_damage)
    Enemy->>Enemy: current_hp -= final_damage
    Game->>Enemy: is_alive()
    Enemy-->>Game: bool

    Note over Main,Enemy: Runda walki - atak wroga (jeśli żyje)
    alt enemy is alive
        Game->>Enemy: base_attack()
        Enemy->>Die: roll(enemy_damage_die)
        Die-->>Enemy: base_damage
        Enemy-->>Game: base_damage

        Game->>CS: CombatStrategy()
        Game->>CS: define_strategy()
        Note over CS,Strategy: Powtórzenie procesu Strategy Pattern
        Game->>CS: attack(base_damage)
        CS->>Strategy: calculate_damage(base_damage)
        Strategy-->>CS: final_damage
        CS-->>Game: final_damage

        Game->>Game: actual_damage = max(0, final_damage - player_armor)
        Game->>Player: take_damage(actual_damage)
        Player->>Player: current_hp -= actual_damage
    end

    Game-->>Main: combat continues or ends
```

## 3. Diagram sekwencji - Pełny przebieg gry

```mermaid
sequenceDiagram
    participant User as Użytkownik
    participant Main as main()
    participant Game as Game
    participant Player as Player
    participant EF as EnemyFactory
    participant Enemy as Enemy

    User->>Main: uruchomienie gry
    Main->>User: input("Name yourself: ")
    User-->>Main: "Hero"

    Main->>Game: Game(player_name="Hero")
    Game->>Player: Player(player_name="Hero")
    Player->>Player: roll HP (1d6)
    Player-->>Game: player instance
    Game-->>Main: game instance

    Main->>Player: roll_equipment()
    Player->>Player: roll 1d6 → get Equipment
    Player->>Player: assign weapon/armor
    Player-->>Main: equipment assigned

    Main->>Game: start()
    Game->>Game: is_game_running = True

    loop while game.is_game_running
        Main->>Game: enter_room()
        Game->>Game: roll room type

        alt RoomType.BOOK
            Game-->>User: "You found the book! YOU WIN!"
            Main->>Game: is_game_running = False
        else RoomType.EMPTY
            Game-->>User: "Nothing here. Moving on..."
        else RoomType.ENEMY
            Game->>EF: create_enemy()
            EF-->>Game: enemy
            Main->>Game: combat(player, enemy)

            loop while both alive
                Note over Game,Enemy: Wymiana ciosów
            end

            alt player dead
                Game-->>User: "You died! GAME OVER"
                Main->>Game: is_game_running = False
            else enemy dead
                Game-->>User: "You won the fight!"
            end
        end
    end

    Main-->>User: koniec gry
```

## Kluczowe obserwacje

### Factory Pattern (Diagram 1)
1. **Separacja odpowiedzialności**: `Game` nie musi wiedzieć, jak tworzyć konkretne typy wrogów
2. **Jednolity interfejs**: `create_enemy()` zawsze zwraca obiekt typu `Enemy`
3. **Losowość kontrolowana**: Fabryka używa `SingleDie` i `ENEMY_TABLE` do losowania typu

### Strategy Pattern (Diagram 2)
1. **Dynamiczny wybór**: Strategia wybierana w runtime na podstawie rzutu 2d6
2. **Brak if-else**: Zamiast wielu warunków, używamy polimorfizmu
3. **Reużywalność**: Ta sama strategia dla gracza i wroga
4. **Separation of concerns**: `CombatStrategy` odpowiada za wybór, `AttackOutcome` za kalkulację

### Przepływ gry (Diagram 3)
1. **Inicjalizacja**: Tworzenie gracza i losowanie ekwipunku
2. **Pętla główna**: Eksploracja pokoi aż do wygranej lub śmierci
3. **Warunki końcowe**: Znalezienie książki (wygrana) lub śmierć gracza (przegrana)
