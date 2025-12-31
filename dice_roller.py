import random

class SingleDie:
    @staticmethod
    def roll(die_type: int) -> int:
        if die_type not in (2, 4, 6, 8, 10, 12, 20, 100):
            raise ValueError(f"Incorrect die value: {die_type}. Please stick to a standard dice notation (2, 4, 6, 8, 10, 12, 20, 100).")
        result = random.randrange(1, die_type+1)
        print(f"Die rolled: 1d{die_type}, result:{result}")
        return result
