from games.game import Game
from display import Display
import random
import time

class Jackpot(Game):
    def __init__(self, player):
        super().__init__(player)
        self.symbols = ["🍒", "🍋", "🍀", "7️⃣ ", "⭐"]

    def play(self):
        bet = self.place_bet()
        if not bet:
            return

        result, content = self.spin(bet)
        matches		    = self.check_matches(result)

        if matches > 0:
            prize   = bet * matches * 5
            self.player.win(prize)
            content += f'  You won {prize} chips!'
        else:
            content += '  You lost!'

        content += '\n\n  1. Play again\n  0. Exit\n'

        if Display.show(self.player, content) == 1:
            self.play()

    def rules(self):
        content = """Jackpot Rules:

  - Jackpot is a slot machine game.
  - You can bet any amount of chips.
  - You have a match if a row or column has the same symbol.
  - The prize is 5 times your bet multiplied by each match!

  Good luck!

  Press Enter to continue...
  	    """
        Display.show(self.player, content)

    def spin(self, bet):
        result  = self.spin_frames(bet)
        content = f"""
                        Result:\n
                        {'\n                        '.join([' | '.join(line) for line in result])}"""

        content += f'\n\n  Bet: {bet}\n'

        return (result, content)


    def spin_frames(self, bet):
        for _ in range(10):
            result  = [self.spin_line() for _ in range(3)]
            content = f"""
                        Spinnig...\n
                        {'\n                        '.join([' | '.join(line) for line in result])}"""

            content += f'\n\n  Bet: {bet}\n'

            Display.show(self.player, content, False)
            time.sleep(0.1)

        return result

    def spin_line(self):
        return [random.choice(self.symbols) for _ in range(3)]

    def check_matches(self, result):
        matches = 0

        for line in result:
            if line[0] == line[1] == line[2]:
                matches += 1

        for col in range(3):
            if result[0][col] == result[1][col] == result[2][col]:
                matches += 1

        return matches
