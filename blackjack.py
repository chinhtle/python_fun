from __future__ import print_function
import random

BANK_DEFAULT_BUYIN = 100


def get_user_response(input_request):
    """
    Prints the request and asks user for their y/n input.
    Returns True if user inputs 'y' and False if user inputs 'n'.
    """
    while True:
        player_move = raw_input("{}: ".format(input_request)).lower()

        if player_move[0] == "y":
            return True
        elif player_move[0] == "n":
            return False
        else:
            print("Please enter a valid input.")


class Table(object):
    """
    Black jack table for managing players and starting the game.
    """
    def __init__(self):
        self.players = set([])
        self.dealer = Dealer(self)

    def add_player(self, player):
        """
        Adds a player to the set of players at the table.
        """
        self.players.add(player)
        print("{} has joined the table!".format(player.name))

    def remove_player(self, player):
        """
        Removes a player from the set of players at the table.
        """
        self.players.remove(player)
        print("{} has left the table!".format(player.name))

    def get_player_stats(self):
        """
        Gets all players' total stats and money.
        """
        print("Players' stats:")
        for player in self.players:
            print("{} has cash:{}, wins:{}, busts:{}, losses:{}".format(
                  player.name, player.bank, player.wins, player.busts,
                  player.losses))

    def start_game(self):
        """
        Begins a game of black jack in a loop.
        """
        if not self.players:
            print("No players have joined the table.")
            return

        print("\nA game of black jack has commenced!")

        while True:
            if not self.dealer.start_round():
                continue

            print("")
            self.dealer.deal_hands()
            print("")
            self.dealer.pay_winners()
            print("")
            self.get_player_stats()
            print("")

            if not get_user_response("Would you like to play again? [y/n]"):
                print("Thanks for playing!")
                break


class Player(object):
    """
    A class for a player, which holds the player's states and bank information.
    """
    def __init__(self, name, bank=BANK_DEFAULT_BUYIN):
        self.name = name
        self.bank = bank
        self.table = None
        self.busted = False
        self.cards = []
        self.wins = 0
        self.losses = 0
        self.busts = 0
        self.bet_amount = 0
        self.active = False

    def collect_winnings(self, amount):
        """
        Collects winnings and adds to the bank.
        """
        self.bank += amount
        print("{} now has {}!".format(self.name, self.bank))

    def bet_money(self, amount):
        """
        Bets an amount by subtracting from the bank and storing the bet amount.
        The bet amount is used later for collecting earnings.
        """
        if not amount or amount > self.bank:
            raise ValueError

        self.bet_amount = amount
        self.bank -= amount
        print("{} has bet {}!".format(self.name, self.bet_amount))

    def join_table(self, table):
        """
        Joins a table. If already in a table, then leave the existing table.
        """
        if self.table:
            self.leave_table()

        self.table = table
        self.table.add_player(self)

    def leave_table(self):
        """
        Leaves the current table the player is seated at.
        """
        if self.table:
            self.table.remove_player(self)
        else:
            print("Not currently playing at any tables.")

    def get_hand(self, card):
        """
        Obtain and append the hand that the dealer serves.
        """
        self.cards.append(card)
        print("{} has received the hand {}".format(self.name, card))
        print("{}'s total is {}".format(self.name, self.get_cards_value()))

    def reset(self):
        """
        Resets the player's states and cards.
        """
        self.busted = False
        self.cards = []
        self.bet_amount = 0
        self.active = False

    def get_cards_value(self):
        """
        Gets the total cards value while also taking into account the value
        of aces, which may be 1 or 11. An ace is a 1 if the total value is
        greater than 21.
        """
        total_value = sum(self.cards)
        if total_value > 21 and 11 in self.cards:
            total_value -= 10

        return total_value

    def buy_chips(self):
        """
        Simulates buying chips by simply resetting the bank amount.
        """
        self.bank = BANK_DEFAULT_BUYIN
        print("{} has bought {} more chips!".format(self.name, self.bank))


class Dealer(Player):
    """
    Dealer class deriving from the player class. Main driver of the game.
    """
    def __init__(self, table):
        Player.__init__(self, "Dealer", 0)
        self.table = table
        self.deck = Deck()
        self.deck.shuffle()

    def start_round(self):
        """
        Begins a new round of black jack.
        Returns true if no issues. False if a round could not be started.
        """
        if not self.reset_and_get_all_bets():
            print("There are currently no active players. Skipping round.")
            return False

        # Deal dealer hand first
        self.deal_card(self)
        self.deal_card(self)
        print("")

        # Deal new cards
        for player in self.table.players:
            self.deal_card(player)
            self.deal_card(player)
            print("")

        return True

    def reset_and_get_all_bets(self):
        """
        Resets all player states and cards and obtains bets.
        Returns whether there are any active players. There may be no active
        players if there are no players or if all players have run out of money
        and wish not to purchase more chips.
        """
        self.reset()

        # Reset any states, cards, and deal new cards
        active_players = False
        for player in self.table.players:
            player.reset()

            # Check if player still has any money left
            if player.bank <= 0:
                print("Sorry, {}, you need money to play!".format(player.name))

                if get_user_response("Would you like to buy more chips?"):
                    player.buy_chips()
                else:
                    # TODO: For now, skipping, which would result in the player
                    # being asked again whether they'd like to buy more chips.
                    # In the future, the user should leave the table or become
                    # a spectator.
                    print("Maybe you'll change your mind on the next round!")
                    self.active = False
                    continue

            self.get_player_bet(player)
            active_players = True
            print("")

        return active_players

    def get_player_bet(self, player):
        """
        Obtains a player's bet.
        """
        while True:
            try:
                output = "How much would you like to bet, "
                output += "{}? (1-{}): ".format(player.name, player.bank)
                bet_amount = int(raw_input(output))
                player.bet_money(bet_amount)
            except ValueError:
                print("Please enter a valid range.")
            else:
                player.active = True
                break

    def deal_hands(self):
        """
        Deal hands to all players followed by the dealer.
        """
        print("Dealing hands...")

        for player in [p for p in self.table.players if p.active]:
            while True:
                player_move = self.get_player_move(player)
                if player_move:
                    self.deal_card(player)

                    if self.check_is_busted(player):
                        print("{} has busted!".format(player.name))
                        player.busted = True
                        break
                else:
                    print("{} refuses to hit!".format(player.name))
                    break

            print("")

        while self.get_cards_value() < 17:
            self.deal_card(self)

            if self.check_is_busted(self):
                print("Dealer has busted!")
                self.busted = True
                break

    def pay_winners(self):
        """
        Updates all player statuses and provide payout to winners.
        """
        print("Here comes the payout!")

        for player in self.table.players:
            status = ""
            if player.busted:
                player.busts += 1
                status = "busted"
            elif not self.busted and \
                    player.get_cards_value() < self.get_cards_value():
                player.losses += 1
                status = "lost"
            else:
                player.wins += 1
                status = "won"
                player.collect_winnings(player.bet_amount * 2)

            print("{} has {}".format(player.name, status))

    def deal_card(self, player):
        """
        Obtains a card from the deck to deal to the player. If there
        are no more cards left in the deck, create a new shuffled deck.
        """
        print("Dealing card...")

        # If card not initialized or runs out, create a new deck and shuffle it
        if not self.deck:
            self.deck = Deck()
            self.deck.shuffle()

        player.get_hand(self.deck.pop())

    def check_is_busted(self, player):
        """
        Checks if the player has busted. If the total card value is greater
        than 21, then it is a bust.
        """
        return player.get_cards_value() > 21

    def get_player_move(self, player):
        """
        Asks the user if they would like to hit or pass. Obtain the users
        response as a "y" or "no" and returns a True or False, respectively.
        """
        print("{}, your total is: {}".format(player.name,
                                             player.get_cards_value()))

        return get_user_response("Would you like to hit? [y/n]")


class Deck(object):
    """
    A deck of cards represented in integers. Since suits don't really matter,
    there are 4 instances of each card number. Card numbers 1-10 are as is,
    i.e.: 1, 1, 1, 1, 2, 2, 2, 2, ... 10, 10, 10, 10

    Jacks, queens, kings are represented as 10. There are 4 instances of each.

    Aces are represented as 11. There are 4 instances.
    """
    def __init__(self):
        self.cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] * 4  # * 4 for all suits
        self.cards += [10] * 4 * 3  # Jacks, queens, and kings
        self.cards += [11] * 4  # Aces
        self.total_cards = len(self.cards)

    def shuffle(self):
        """
        Algorithm for shuffling the card. Iterate through each index and
        swap it with a random index.
        """
        for index, value in enumerate(self.cards):
            card_to_swap = index

            # Get a random index that is not equal to current card index
            while card_to_swap == index:
                card_to_swap = random.randint(0, self.total_cards - 1)

            self.cards[index] = self.cards[card_to_swap]
            self.cards[card_to_swap] = value

        # NOTE: There is already a shuffle built in.
        # random.shuffle(self.cards)

    def pop(self):
        """
        Obtain the card at the top of the stack.
        """
        return self.cards.pop()


def main():
    """
    Start a game of black jack by adding users to the table.
    """
    black_jack_table = Table()

    while True:
        player_name = raw_input("Add a player to the table by name: ")
        Player(player_name).join_table(black_jack_table)

        if not get_user_response("Add another player? [y/n]"):
            break

        print("")

    black_jack_table.start_game()


if __name__ == "__main__":
    main()
