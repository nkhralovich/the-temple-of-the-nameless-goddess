from abc import ABC
from dice_roller import SingleDie
from enum import Enum


class EnemyType(Enum):
    RAT = "rat"
    ZOMBIE = "zombie"
    SKELETON = "skeleton"


ENEMY_TABLE = {
    1: EnemyType.ZOMBIE,
    2: EnemyType.SKELETON,
    3: EnemyType.RAT,
    4: EnemyType.RAT,
    5: EnemyType.SKELETON,
    6: EnemyType.ZOMBIE,
}


class Enemy(ABC):
    """
    Klasa abstrakcyjna dla tworzenia wrogów
    """

    def __init__(self, enemy_name: str, enemy_max_hp: int, enemy_damage_die: int):
        self.enemy_name = enemy_name 
        self.enemy_max_hp = enemy_max_hp
        self.enemy_damage_die = enemy_damage_die
        self.enemy_current_hp = enemy_max_hp

    def is_alive(self) -> bool:
        return self.enemy_current_hp > 0

    def base_attack(self) -> int:
        attack_outcome = SingleDie.roll(die_type= self.enemy_damage_die)
        return attack_outcome
    
    def take_damage(self, damage_taken: int):
        self.enemy_current_hp = self.enemy_current_hp - damage_taken

    def __str__(self) -> str:
          """Reprezentacja tekstowa wroga"""
          return f"{self.enemy_name} (HP: {self.enemy_current_hp}/{self.enemy_max_hp})"
    


class Rat(Enemy):
    """
    Szczur -- mały wróg
    """
    def __init__(self):
        super().__init__(
            enemy_name="Big filthy rat",
            enemy_max_hp = 1,
            enemy_damage_die = 2
        )



class Skeleton(Enemy):
    """
    Szkielet -- średni wróg
    """
    def __init__(self):
        super().__init__(
            enemy_name="Shaky old skeleton",
            enemy_max_hp = 2,
            enemy_damage_die = 6
        )

    def base_attack(self) -> int:
        attack_value = SingleDie.roll(die_type= self.enemy_damage_die)
        return attack_value // 2


class Zombie(Enemy):
    """
    Zombie -- duży silny wróg
    """
    def __init__(self):
        super().__init__(
            enemy_name="Ugly rotten zombie",
            enemy_max_hp = 3,
            enemy_damage_die = 6
        )


    def base_attack(self) -> int:
        attack_value = SingleDie.roll(die_type= self.enemy_damage_die)
        return attack_value + 1


class EnemyFactory:
    """
    Factory Pattern do łatwego tworzenia wrogów
    """
    ENEMY_CLASS_MAPPING = {
        EnemyType.RAT: Rat,
        EnemyType.SKELETON: Skeleton,
        EnemyType.ZOMBIE: Zombie
    }


    @staticmethod
    def create_enemy() -> Enemy:
        roll = SingleDie.roll(die_type=6)
        enemy_type = ENEMY_TABLE[roll] # zwraca EnemyType
        enemy = EnemyFactory.ENEMY_CLASS_MAPPING.get(enemy_type)

        if enemy:
            return enemy()
        return None
