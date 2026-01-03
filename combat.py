from dice_roller import SingleDie
from damage import *

class AttackResolver:
    @staticmethod
    def map_combat_strategy(roll: int):
        if roll == 12:
            return CritStrategy()
        elif roll >= 10:
            return FullHitStrategy()
        elif 7 <= roll <= 9:
            return GlancingBlowStrategy()
        else:  # roll <= 6
            return MissStrategy()


class CombatStrategy:
    def __init__(self):
        self.combat_strategy = None 

    def define_strategy(self):
        strategy_roll = SingleDie.roll_2d6()
        self.combat_strategy = AttackResolver.map_combat_strategy(strategy_roll)

    
    def attack(self, base_damage):
        final_damage =  self.combat_strategy.calculate_damage(base_damage)
        return final_damage

