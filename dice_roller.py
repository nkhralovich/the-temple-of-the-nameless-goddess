import random

class SingleDie:
    def __init__(self, die_type):
        if die_type not in (2, 4, 6, 8, 10, 12, 20, 100):
            raise ValueError(f"Incorrect die value: {die_type}. Please stick to a standard dice notation (2, 4, 6, 8, 10, 12, 20, 100).")
        self.die_type = die_type


    def roll(self):
        result = random.randrange(1, self.die_type+1)
        print(f"Die rolled: 1d{self.die_type}, result:{result}")
        return result


class DiceRoller:
    def __init__(self, die_type, number_of_dice):
        self.die = SingleDie(die_type)
        self.number_of_dice = number_of_dice
        if number_of_dice < 2:
            raise ValueError(f"Incorrect dice number value: {number_of_dice}. The amount of dice should be >= 2. Use SingleDie class.")
        
    def roll_multiple(self) -> list[int]:
        dice_array = [self.die.roll() for _ in range(self.number_of_dice)]
        print(f"Dice rolled: {self.number_of_dice}d{self.die.die_type}, result:{dice_array}")
        return dice_array
    
    def get_total(self) -> int:
        dice_sum = sum(self.roll_multiple())
        print(f"Dice results sum: {dice_sum}")
        return dice_sum

