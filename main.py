from dice_roller import SingleDie, DiceRoller
from player import Player
from room import RoomType



class Game:
    def __init__(self, player_name):
        self.player = Player(name=player_name)
        self.is_game_running = False
        self.nr_of_chambers = 0

    def start(self):
         self.is_game_running = True

    
    def enter_room(self):
        print("room")



def main():
    name = input("Hello, brave adventurer! Name yourself: ")
    die = SingleDie(6)
    result = die.roll()
    print(f"Great, {name}! Your roll is:")
    print(result)



if __name__ == '__main__':
    main()