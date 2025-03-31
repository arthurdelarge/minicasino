import random

class Player:
    def __init__(self):
        self.name        = input('What is your name? ')
        self.chips       = input('How many chips do you want? ')
        self.chips       = int((self.chips.isdigit() and self.chips))
        self.tickets     = []
        self.game_credit = 0

    def give_chips(self, quantity):
        if quantity < 1 or quantity > self.chips:
            return False
        else:
            self.chips       -= quantity
            self.game_credit += 1
            self.update_tickets()
            return True

    def win(self, quantity):
        self.chips += quantity

    def info(self):
        return (self.name, self.chips, len(self.tickets) )

    def update_tickets(self):
        if self.game_credit // 5 == 0:
            return

        self.game_credit -= 5

        if len(self.tickets) < 5:
            self.tickets.append(random.sample(range(1, 26), 5))

    def reset_tickets(self):
        self.tickets = []

    def add_chips(self, quantity):
        self.chips += quantity
