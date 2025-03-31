from games.game import Game
from display import Display
import random
import time

class Lottery(Game):
	def __init__(self, player):
		super().__init__(player)

	def play(self):
		if len(self.player.tickets) < 1:
			return Display.show(self.player, '  You dont have any tickets yet!\n')

		if self.confirm_action() != 1:
			return

		result, content = self.raffle()

		matches     = self.check_matches(result)
		len_matches = len(matches)

		if len_matches > 0:
			prize = 5 * (2 ** (len_matches - 1))
			self.player.win(prize)
			content += f'  Matched numbers: {matches}\n\n'
			content += f'  You won {prize} chips!\n'
		else:
			content += '  You lost!\n'

		self.player.reset_tickets()
		Display.show(self.player, content)

	def rules(self):
		content = """Lottery Rules:

  - Each 5 plays you gain a ticket of 5 numbers (1 to 25).
  - You can use your ticket at any time.
  - A ticket can be used only one time.
  - You get 1 chip if you match the first number.
  - Each next match multiplies your prize by 2.
  - When you hold tickets the multiplier potential grows.
  - The limit of tickets you can hold is 5.

  Good luck!

  Press Enter to continue...
		"""

		Display.show(self.player, content)

	def confirm_action(self):
		content  = '  Are you sure you want to use your tickets?\n'
		content += '  If you hold more tickets you will have better chances.\n\n'
		content += f'  Your tickets:\n\n    {'\n    '.join(str(ticket) for ticket in self.player.tickets)}\n\n'
		content += '  1. Use your tickets\n  0. Hold more tickets\n'

		return Display.show(self.player, content)

	def raffle(self):
		result 	= self.raffle_frames()
		content = f'  Result: {result}\n\n'
		content += f'  Your tickets:\n\n    {'\n    '.join(str(ticket) for ticket in self.player.tickets)}\n\n'

		return (result, content)

	def raffle_frames(self):
		result = random.sample(range(1, 25), 5)

		for i in range(5):
			content = f'  Result: {result[:i]}\n\n'
			content += f'  Your tickets:\n\n    {'\n    '.join(str(ticket) for ticket in self.player.tickets)}\n\n'

			Display.show(self.player, content, False)
			time.sleep(1)

		return result

	def check_matches(self, result):
		matches = []

		for number in result:
			for ticket in self.player.tickets:
				if number in ticket:
					matches.append(number)

		return matches

