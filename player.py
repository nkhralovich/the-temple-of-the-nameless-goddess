from dice_roller import SingleDie
from equipment import EquipmentType, EQUIPMENT_TABLE


class Player:
    def __init__(self, player_name: str):
        hp_die = SingleDie(die_type=6)
        self.max_hp = hp_die.roll()
        self.player_name = player_name
        self.current_hp = self.max_hp
        self.player_armor = 0 # reprezentuje wartość odejmowaną od obrażeń
        self.player_weapon = 2 # reprezentuje kostkę, nie 2 obrażenia!

        print(f"Player created! HP: {self.max_hp}, armor: {self.player_armor}, weapon die: d{self.player_weapon}")

    def roll_equipment(self) -> None:
        equipment_die = SingleDie(die_type=6)
        roll_for_equipment = equipment_die.roll() #tu losujemy ekwipunek
        equipment = EQUIPMENT_TABLE[roll_for_equipment] # sprawdzamy wynik losowania w słowniku equipment
        print(f"Your starting equipment is {equipment.description}. Congrats!")
        if equipment.equipment_type == EquipmentType.WEAPON:
            self.player_weapon = equipment.die
        elif equipment.equipment_type  ==  EquipmentType.ARMOR:
            self.player_armor = equipment.die
        else:
            print("Nothing for you today!")
    
    def is_alive(self) -> bool:
        return self.current_hp > 0
    
    def take_damage(self, damage_taken: int):
        self.current_hp = self.current_hp - damage_taken

    def base_attack(self, player_weapon: int):
        return SingleDie.roll(player_weapon)


