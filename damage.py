
from abc import ABC, abstractmethod

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
    