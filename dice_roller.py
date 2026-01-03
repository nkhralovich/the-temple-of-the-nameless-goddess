import random

class SingleDie:
    @staticmethod
    def roll(die_type: int) -> int:
        if die_type not in (2, 4, 6, 8, 10, 12, 20, 100):
            raise ValueError(f"Incorrect die value: {die_type}. Please stick to a standard dice notation (2, 4, 6, 8, 10, 12, 20, 100).")
        result = random.randrange(1, die_type+1)
        return result

    @staticmethod
    def roll_2d6() -> int:
        """Roll 2d6 and return the sum"""
        return random.randrange(1, 7) + random.randrange(1, 7)
