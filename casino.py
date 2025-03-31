from display import Display
from games.jackpot import Jackpot
from games.lottery import Lottery
from player import Player

class Casino:
    def __init__(self):
        self.player = Player()

    def start(self):
        stage = 1
        while stage:
            stage = self.menu()
            match stage:
                case 1:
                    Jackpot(self.player).start()
                    continue
                case 2:
                    Lottery(self.player).start()
                case 3:
                    self.player.add_chips(Display.get_chips())

        print('\nGoodbye!')

    def menu(self):
        options = [
            "1. Jackpot",
            "2. Lottery",
            "0. Exit"
        ]

        content = ''.join([f"   {option}\n" for option in options])

        return Display.show(self.player, content)
