from dice_roller import SingleDie
from equipment import EquipmentType, EQUIPMENT_TABLE


class Player:
    def __init__(self, max_hp):
        hp_die = SingleDie(die_type=6)
        self.max_hp = hp_die.roll()
        self.current_hp = max_hp
        self.armor_die = 0
        self.damage_die = 1

        print(f"Player created! HP: {self.max_hp}, armor: {self.armor}, damage: {self.damage}")

    def roll_equipment(self) -> None:
        equipment_die = SingleDie(die_type=6)
        equipment_key = equipment_die.roll()
        equipment = EQUIPMENT_TABLE[equipment_key]
        print(f"Your starting equipment is {equipment["description"]}. Congrats!")
        if equipment["equipment_type"] == EquipmentType.WEAPON:
            self.damage_die = self.damage + equipment["die"]
        elif equipment["die"] ==  EquipmentType.ARMOR:
            self.armor_die = equipment["die"]
        else:
            print("Nothing for you today!")
    
    def is_alive(self) -> bool:
        return self.current_hp > 0
    
    def take_damage(self, damage):
        self.current_hp = self.current_hp - damage


