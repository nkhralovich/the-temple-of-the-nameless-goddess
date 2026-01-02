from dice_roller import SingleDie
from player import Player
from room import RoomType, ROOM_TABLE
from enemy import EnemyFactory
from combat import Combat, AttackResolver



class Game:
    def __init__(self, player_name):
        self.player = Player(name=player_name)
        self.is_game_running = False
        self.nr_of_chambers = 0

    def start(self):
         self.is_game_running = True


    def combat(player, enemy):
        print("The enemy attacks!")
        while enemy.is_alive() and player.is_alive():
            player_combat = Combat()
            player_combat.define_strategy()
            base_damage = player.base_attack()
            final_damage = player_combat.attack(base_damage)
            enemy.take_damage(final_damage)



    
    def enter_room(self):
        room_type = SingleDie.roll(die_type=6)

        if ROOM_TABLE[room_type] == RoomType.ENEMY:
            print(f"You see rows of sealed stone coffins. Something moves in the shadows — not alive, but not quite at peace either.")
            return EnemyFactory.create_enemy()
        if ROOM_TABLE[room_type] == RoomType.EMPTY:
            print(f"Nothing to do here.")
            pass
        if ROOM_TABLE[room_type] == RoomType.BOOK:
            print(f"You see a big room, moss on the walls, heavy air, and an ancient altar at the center. It is dark, but you can guess the book lies on the altar, among dust, scattered chalices and candles that extinguished long ago. Come get your book, you lucky bastard! And get out of here.")
            pass


def main():
    print("=== Welcome to The Temple of The Nameless Goddess ===")
    name = input("Hello, brave adventurer! Name yourself: ")
    print(f"Welcome, {name}! Your goal: get the artifact placed in the Main Crypt Chamber before the enemies get you. Good luck!")

    player = Player(player_name=name)
    player.roll_equipment()

    game_running = True

    while game_running:
        pass


if __name__ == '__main__':
    main()