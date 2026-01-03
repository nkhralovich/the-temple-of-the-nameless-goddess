from dice_roller import SingleDie
from player import Player
from room import RoomType, ROOM_TABLE
from enemy import EnemyFactory
from combat import CombatStrategy



class Game:
    def __init__(self, player_name):
        self.player = Player(player_name=player_name)
        self.is_game_running = False
        self.nr_of_chambers = 0

    def start(self):
         self.is_game_running = True

    @staticmethod
    def combat(player, enemy):
        print("The enemy tries to attack, but you have better reaction and attack first.")
        while enemy.is_alive() and player.is_alive():

            player_base_damage = player.base_attack()
            player_combat = CombatStrategy()
            player_combat.define_strategy()
            player_final_damage = player_combat.attack(player_base_damage)
            enemy.take_damage(player_final_damage)
            print(f"Enemy takes {player_final_damage} damage.")

            if not enemy.is_alive():
                print("You won!")
                break

            enemy_base_damage = enemy.base_attack()
            enemy_combat = CombatStrategy()
            enemy_combat.define_strategy()
            enemy_final_damage = enemy_combat.attack(enemy_base_damage)
            actual_damage = max(0, enemy_final_damage - player.player_armor) 
            player.take_damage(actual_damage)
            print(f"You take {actual_damage} damage.")

            if not player.is_alive():
                print("You died!")


    @staticmethod
    def enter_room():
        room_type_roll = SingleDie.roll(die_type=6)
        room_type = ROOM_TABLE[room_type_roll]
        print("You enter a room...")

        if room_type == RoomType.ENEMY:
            print(f"You see rows of sealed stone coffins. Something moves in the shadows — not alive, but not quite at peace either.")
            enemy = EnemyFactory.create_enemy()
            if enemy:
                print(f"Your eyes are adjusted to darkness and you see a {enemy.enemy_name}!")
                return room_type, enemy
            else:
                # Fallback to empty room if enemy creation failed
                print("The shadows settle. It was nothing after all.")
                return RoomType.EMPTY, None
        if room_type == RoomType.EMPTY:
            return room_type, None
        if room_type == RoomType.BOOK:
            return room_type, None


def main():
    print("=== Welcome to The Temple of The Nameless Goddess ===")
    name = input("Hello, brave adventurer! Name yourself: ")
    print(f"Welcome, {name}! Your goal: get the artifact placed in the Main Crypt Chamber before the enemies get you. Good luck!")

    game = Game(player_name=name)
    game.player.roll_equipment()
    game.start()

    while game.is_game_running:
        room_type, enemy = Game.enter_room()
        if room_type == RoomType.BOOK:
            print(f"You see a big room, moss on the walls, heavy air, and an ancient altar at the center. It is dark, but you can guess the book lies on the altar, among dust, scattered chalices and candles that extinguished long ago. Come get your book, you lucky bastard! And get out of here.")
            game.is_game_running = False
        elif room_type == RoomType.ENEMY:
            Game.combat(game.player, enemy)
            if not game.player.is_alive():
                game.is_game_running = False
        elif room_type == RoomType.EMPTY:
            print("Nothing here. Moving  to the next room.")



if __name__ == '__main__':
    main()