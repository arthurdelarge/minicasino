from display import Display

class Game:
	def __init__(self, player):
		self.name   = type(self).__name__
		self.player = player


	def start(self):
		stage = 1
		while stage:
			stage = self.menu()
			match stage:
				case 1:
					self.play()
				case 2:
					self.rules()

	def menu(self):
		options = [
			"1. Play",
			"2. Rules",
			"0. Exit"
		]

		content = f"  {self.name}: \n\n" + ''.join([f"   {option}\n" for option in options])

		return Display.show(self.player, content)

	def play(self):
		pass

	def rules(self):
		pass

	def place_bet(self):
		bet = Display.get_bet()

		if not self.player.give_chips(bet):
			Display.invalid_bet(self.player)
			return 0

		return bet
