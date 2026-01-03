from dice_roller import SingleDie
from equipment import EquipmentType, EQUIPMENT_TABLE


class Player:
    def __init__(self, player_name: str):
        self.max_hp = SingleDie.roll(die_type=6)
        self.player_name = player_name
        self.current_hp = self.max_hp
        self.player_armor = 0 
        self.player_weapon = 2 

        

    def roll_equipment(self) -> None:
        roll_for_equipment = SingleDie.roll(die_type=6) 
        equipment = EQUIPMENT_TABLE[roll_for_equipment]
        print(f"Your starting equipment is {equipment.description}. Congrats!")
        if equipment.equipment_type == EquipmentType.WEAPON:
            self.player_weapon = equipment.die
        elif equipment.equipment_type  ==  EquipmentType.ARMOR:
            self.player_armor = equipment.die
        print(f"Player created! HP: {self.max_hp}, armor: {self.player_armor}, weapon die: d{self.player_weapon}")
    
    def is_alive(self) -> bool:
        return self.current_hp > 0
    
    def take_damage(self, damage_taken: int):
        self.current_hp = self.current_hp - damage_taken

    def base_attack(self):
        return SingleDie.roll(self.player_weapon)


