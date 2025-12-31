from dice_roller import SingleDie
from damage import *

class AttackResolver:
    @staticmethod
    def map_combat_strategy(roll: int):
        if roll <=5:
            return MissStrategy()
        elif 6 <= roll <= 8:
            return GlancingBlowStrategy()
        elif 9 <= roll <= 11:
            return FullHitStrategy()
        else: 
            return CritStrategy()


class Combat:
    def __init__(self):
        self.combat_strategy = None 

    def define_strategy(self):
        strategy_roll = SingleDie.roll(die_type=12) # zwraca int
        self.combat_strategy = AttackResolver.map_combat_strategy(strategy_roll)

    
    def attack(self, base_damage):
        final_damage =  self.combat_strategy.calculate_damage(base_damage)
        return final_damage

