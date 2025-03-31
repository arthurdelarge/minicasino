from os import system, name

class Display:
    @staticmethod
    def show(player, content = '', options=True):
        Display.header()
        print(content)
        Display.footer(player.info())

        return Display.get_option() if options else None

    @staticmethod
    def header():
        Display.clear()
        print("""
    ▗▖  ▗▖▄ ▄▄▄▄  ▄      ▗▄▄▖▗▞▀▜▌ ▗█▄▖▄ ▄▄▄▄   ▄▄▄
    ▐▛▚▞▜▌▄ █   █ ▄     ▐▌   ▝▚▄▟▌▐▌█  ▄ █   █ █   █
    ▐▌  ▐▌█ █   █ █     ▐▌         ▝█▚▖█ █   █ ▀▄▄▄▀
    ▐▌  ▐▌█       █     ▝▚▄▄▖     ▗▄█▞▘█
                                        ▀

    🎲 Blackjack • Three Card Poker • Jackpot • Lottery 🎰""")
        print("=" * 60 + "\n")

    @staticmethod
    def footer(player_info):
        name, chips, tickets = player_info

        print("=" * 60 + "\n")
        print(f"     Player: {name} | Chips: {chips} | Lottery Tickets: {tickets}\n")
        print("=" * 60 + "\n")

    @staticmethod
    def get_option():
        option = input("Action: ")
        return int(option.isdigit() and option)

    @staticmethod
    def clear():
        system('cls' if name == 'nt' else 'clear')

    @staticmethod
    def get_bet():
        bet = input("Enter your bet: ")
        return int(bet.isdigit() and bet)

    @staticmethod
    def get_chips():
        bet = input("How many chips do you want? ")
        return int(bet.isdigit() and bet)

    @staticmethod
    def invalid_bet(player):
        Display.show(player, "  Not enough chips!\n")
