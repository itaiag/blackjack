#!/usr/bin/env python

from random import Random
colors_support = True
try:
    from colorama import init, Fore
    init()
except:
    colors_support = False
    print "For colors install colorama"


hint_table = \
        {('5',): {'A': 'h', '10': 'h', '3': 'h', '2': 'h', '5': 'h', '4': 'h', '7': 'h', '6': 'h', '9': 'h', '8': 'h'},
        ('6',): {'A': 'h', '10': 'h', '3': 'h', '2': 'h', '5': 'h', '4': 'h', '7': 'h', '6': 'h', '9': 'h', '8': 'h'},
        ('7',): {'A': 'h', '10': 'h', '3': 'h', '2': 'h', '5': 'h', '4': 'h', '7': 'h', '6': 'h', '9': 'h', '8': 'h'},
        ('8',): {'A': 'h', '10': 'h', '3': 'h', '2': 'h', '5': 'h', '4': 'h', '7': 'h', '6': 'h', '9': 'h', '8': 'h'},
        ('9',): {'A': 'h', '10': 'h', '3': 'd', '2': 'h', '5': 'd', '4': 'd', '7': 'h', '6': 'd', '9': 'h', '8': 'h'},
        ('10',): {'A': 'h', '10': 'h', '3': 'd', '2': 'd', '5': 'd', '4': 'd', '7': 'd', '6': 'd', '9': 'd', '8': 'd'},
        ('11',): {'A': 'h', '10': 'd', '3': 'd', '2': 'd', '5': 'd', '4': 'd', '7': 'd', '6': 'd', '9': 'd', '8': 'd'},
        ('12',): {'A': 'h', '10': 'h', '3': 'h', '2': 'h', '5': 's', '4': 's', '7': 'h', '6': 's', '9': 'h', '8': 'h'},
        ('13',): {'A': 'h', '10': 'h', '3': 's', '2': 's', '5': 's', '4': 's', '7': 'h', '6': 's', '9': 'h', '8': 'h'},
        ('14',): {'A': 'h', '10': 'h', '3': 's', '2': 's', '5': 's', '4': 's', '7': 'h', '6': 's', '9': 'h', '8': 'h'},
        ('15',): {'A': 'h', '10': 'h', '3': 's', '2': 's', '5': 's', '4': 's', '7': 'h', '6': 's', '9': 'h', '8': 'h'},
        ('16',): {'A': 'h', '10': 'h', '3': 's', '2': 's', '5': 's', '4': 's', '7': 'h', '6': 's', '9': 'h', '8': 'h'},
        ('17',): {'A': 's', '10': 's', '3': 's', '2': 's', '5': 's', '4': 's', '7': 's', '6': 's', '9': 's', '8': 's'},
        ('18',): {'A': 's', '10': 's', '3': 's', '2': 's', '5': 's', '4': 's', '7': 's', '6': 's', '9': 's', '8': 's'},
        ('19',): {'A': 's', '10': 's', '3': 's', '2': 's', '5': 's', '4': 's', '7': 's', '6': 's', '9': 's', '8': 's'},
        ('20',): {'A': 's', '10': 's', '3': 's', '2': 's', '5': 's', '4': 's', '7': 's', '6': 's', '9': 's', '8': 's'},
        ('2', 'A'): {'A': 'h', '10': 'h', '3': 'h', '2': 'h', '5': 'd', '4': 'h', '7': 'h', '6': 'd', '9': 'h', '8': 'h'},
        ('3', 'A'): {'A': 'h', '10': 'h', '3': 'h', '2': 'h', '5': 'd', '4': 'h', '7': 'h', '6': 'd', '9': 'h', '8': 'h'},
        ('4', 'A'): {'A': 'h', '10': 'h', '3': 'h', '2': 'h', '5': 'd', '4': 'd', '7': 'h', '6': 'd', '9': 'h', '8': 'h'},
        ('5', 'A'): {'A': 'h', '10': 'h', '3': 'h', '2': 'h', '5': 'd', '4': 'd', '7': 'h', '6': 'd', '9': 'h', '8': 'h'},
        ('6', 'A'): {'A': 'h', '10': 'h', '3': 'd', '2': 'h', '5': 'd', '4': 'd', '7': 'h', '6': 'd', '9': 'h', '8': 'h'},
        ('7', 'A'): {'A': 'h', '10': 'h', '3': 'd', '2': 's', '5': 'd', '4': 'd', '7': 's', '6': 'd', '9': 'h', '8': 's'},
        ('8', 'A'): {'A': 's', '10': 's', '3': 's', '2': 's', '5': 's', '4': 's', '7': 's', '6': 's', '9': 's', '8': 's'},
        ('9', 'A'): {'A': 's', '10': 's', '3': 's', '2': 's', '5': 's', '4': 's', '7': 's', '6': 's', '9': 's', '8': 's'},
        ('A', 'A'): {'A': 'h', '10': 'h', '3': 'h', '2': 'h', '5': 'h', '4': 'h', '7': 'h', '6': 'h', '9': 'h', '8': 'h'},
        ('2', '2'): {'A': 'h', '10': 'h', '3': 'h', '2': 'h', '5': 'h', '4': 'h', '7': 'h', '6': 'h', '9': 'h', '8': 'h'},
        ('3', '3'): {'A': 'h', '10': 'h', '3': 'h', '2': 'h', '5': 'h', '4': 'h', '7': 'h', '6': 'h', '9': 'h', '8': 'h'},
        ('4', '4'): {'A': 'h', '10': 'h', '3': 'h', '2': 'h', '5': 'h', '4': 'h', '7': 'h', '6': 'h', '9': 'h', '8': 'h'},
        ('5', '5'): {'A': 'h', '10': 'h', '3': 'd', '2': 'd', '5': 'd', '4': 'd', '7': 'd', '6': 'd', '9': 'd', '8': 'd'},
        ('6', '6'): {'A': 'h', '10': 'h', '3': 'h', '2': 'h', '5': 'h', '4': 'h', '7': 'h', '6': 'h', '9': 'h', '8': 'h'},
        ('7', '7'): {'A': 'h', '10': 'h', '3': 'h', '2': 'h', '5': 'h', '4': 'h', '7': 'h', '6': 'h', '9': 'h', '8': 'h'},
        ('8', '8'): {'A': 'h', '10': 'h', '3': 'h', '2': 'h', '5': 'h', '4': 'h', '7': 'h', '6': 'h', '9': 'h', '8': 'h'},
        ('9', '9'): {'A': 's', '10': 's', '3': 'h', '2': 'h', '5': 'h', '4': 'h', '7': 's', '6': 'h', '9': 'h', '8': 'h'},
        ('10', '10'): {'A': 's', '10': 's', '3': 's', '2': 's', '5': 's', '4': 's', '7': 's', '6': 's', '9': 's', '8': 's'}}


def color(color):
    if colors_support:
        if color is "green":
            return Fore.GREEN  # @UndefinedVariable
        elif color is "red":
            return Fore.RED  # @UndefinedVariable
        elif color is "white":
            return Fore.WHITE  # @UndefinedVariable
        elif color is "yellow":
            return Fore.YELLOW  # @UndefinedVariable
        elif color is "blue":
            return Fore.BLUE  # @UndefinedVariable
        else:
            return Fore.WHITE  # @UndefinedVariable
    else:
        return ''


class Bookie(object):

    def __init__(self, credit=1000):
        self.credit = credit
        self.bet = None
        self.previous_bet = None

    def place_bet(self, bet=None, ratio=2):
        if bet is None and self.previous_bet is None:
            raise Exception("No bet was specified")
        if bet is None and self.previous_bet is not None:
            # Using the last bet
            bet = self.previous_bet
        if bet > self.credit:
            raise Exception("There is only {0} in credit\
                , can't place bet of {1}".format(self.credit, bet))
        self.ratio = ratio
        self.previous_bet = bet
        self.bet = bet

    def report_win(self):
        if self.bet is None:
            raise Exception("No bet was placed")
        self.credit += self.bet * self.ratio - self.bet

    def report_lose(self):
        if self.bet is None:
            raise Exception("No bet was placed")
        self.credit -= self.bet

    def double_bet(self):
        if self.bet is None:
            raise Exception("No bet was placed")
        self.bet *= 2

    def half_bet(self):
        if self.bet is None:
            raise Exception("No bet was placed")
        self.bet /= 2

    def abort_bet(self):
        self.bet = 0


class Deck(object):
    def __init__(self, num_of_decks):
        self.cards = []
        self.rand = Random()
        for deck_num in range(num_of_decks * 4):
            self.cards.extend(range(2, 11))
        self.cards.extend(['J'] * 4 * num_of_decks)
        self.cards.extend(['Q'] * 4 * num_of_decks)
        self.cards.extend(['K'] * 4 * num_of_decks)
        self.cards.extend(['A'] * 4 * num_of_decks)

    def get_card(self):
        card_num = self.rand.randint(0, len(self.cards) - 1)
        card = self.cards[card_num]
        del self.cards[card_num]
        return card


class Player(object):
    def __init__(self, deck):
        self.cards = []
        self.deck = deck

    def draw_card_from_deck(self):
        self.cards.append(self.deck.get_card())

    def get_sum_of_cards(self):
        sum_of_cards = 0
        aces = 0
        for card in self.cards:
            # Each one of the faces card is 10
            if card is 'J' or card is 'Q' or card is 'K':
                sum_of_cards += 10
            elif card is 'A':
                aces += 1
            elif card is 'X':
                # Hidden card
                continue
            else:
                sum_of_cards += card
        # We need to see how to handle aces
        if aces > 0:
            temp_sum = 11 + (aces - 1) + sum_of_cards
            if temp_sum <= 21:
                sum_of_cards = temp_sum
            else:
                sum_of_cards += aces
        return sum_of_cards

    def get_cards(self):
        return self.cards


class MachinePlayer(Player):

    def __init__(self, deck):
        super(MachinePlayer, self).__init__(deck)
        self.hidden_card = None

    def should_take_another_card(self, player):
        if self.get_sum_of_cards() < 17 or\
            (self.get_sum_of_cards() is 17 and
                self.cards.count('A') is 1):
            return True
        return False

    def draw_card_from_deck(self):
        if len(self.cards) is 1 and self.hidden_card is None:
            # The second card should be hidden
            self.hidden_card = self.deck.get_card()
            self.cards.append('X')
        elif self.hidden_card is not None:
            # At the third time, the hidden card is shown
            self.cards.remove('X')
            self.cards.append(self.hidden_card)
            self.hidden_card = None
        else:
            self.cards.append(self.deck.get_card())


class Result(object):

    def __init__(self, machine, player):
        self.machine = machine
        self.player = player
        self._player_surrended = False

    def calculate(self, no_more_moves=False):
        if self._player_surrended:
            self.winner = "dealer"
            self.result_type = "surrended"
            self.is_ended = True
            self._player_surrended = False
            return self

        player_score = self.player.get_sum_of_cards()
        dealer_score = self.machine.get_sum_of_cards()

        self.is_ended = False
        self.winner = None
        if player_score is 21 and dealer_score is not 21:
            self.winner = "player"
            self.result_type = "21"
        elif dealer_score is 21 and player_score is not 21:
            self.winner = "dealer"
            self.result_type = 21
        elif dealer_score > 21 and player_score <= 21:
            self.winner = "player"
            self.result_type = "busting"
        elif player_score > 21 and dealer_score <= 21:
            self.winner = "dealer"
            self.result_type = "busting"
        elif no_more_moves:
            if player_score > dealer_score:
                self.winner = "player"
                self.result_type = "score"
            elif dealer_score > player_score:
                self.winner = "dealer"
                self.result_type = "score"
            elif dealer_score is player_score:
                self.winner = "tie"
                self.result_type = "push"
        if self.winner is not None:
            self.is_ended = True
        return self

    def player_surrended(self):
        self._player_surrended = True


class Game(object):

    def __init__(self, bookie, num_of_decks=4):
        self.deck = Deck(num_of_decks)
        self.round = 0
        self.bookie = bookie

    def print_status(self):
        self.round += 1
        print color("white") + "Round {0}".format(self.round)
        print "Dealer got {0} ({1})".format(self.machine.get_cards(),
                                            self.machine.get_sum_of_cards())
        print "You got {0} ({1})".format(self.player.get_cards(),
                                         self.player.get_sum_of_cards())

    def start_game(self):
        self.machine = MachinePlayer(self.deck)
        self.player = Player(self.deck)
        self.result = Result(self.machine, self.player)

        self.player.draw_card_from_deck()
        self.machine.draw_card_from_deck()

        self.player.draw_card_from_deck()
        self.machine.draw_card_from_deck()
        self.print_status()

    def is_game_ended(self, no_more_moves=False):
        if self.result.calculate(no_more_moves).is_ended:
            if self.result.winner is "player":
                print color("green")
                self.bookie.report_win()
            elif self.result.winner is "dealer":
                print color("red")
                self.bookie.report_lose()
            elif self.result.winner is "tie":
                print color("yellow")
                self.bookie.abort_bet()
            if self.result.winner is not "tie":
                print "{0} won due to {1}".\
                    format(self.result.winner, self.result.result_type)
            else:
                print "Push"
        return self.result.is_ended

    def dealer_turn(self):
        self.machine.draw_card_from_deck()
        self.print_status()
        while self.machine.should_take_another_card(self.player):
            self.machine.draw_card_from_deck()
            self.print_status()

    def give_hint(self):
        def normalize(card):
            if card == "J" or card == "Q" or card == "K":
                return str(10)
            return str(card)

        tuple_sum = str(self.player.get_sum_of_cards()),
        card1 = normalize(self.player.cards[0])
        card2 = normalize(self.player.cards[1])
        tuple_cards = tuple(sorted([card1, card2]))
        if tuple_cards in hint_table:
            hint_raw = hint_table[tuple_cards]
        elif tuple_sum in hint_table:
            hint_raw = hint_table[tuple_sum]
        else:
            return "No hint found"
        return hint_raw.get(normalize(self.machine.cards[0]))

    def player_turn(self):
        first = True
        ans = None
        while self.player.get_sum_of_cards() < 20 and ans != "s":
            if first:
                ans = raw_input(color("yellow") + "[H]it, [s]tand, su[r]render,\
[d]ouble or h[e]lp?: ")
            else:
                ans = raw_input(color("yellow") + "[H]it or [s]tand?: ")
            if ans == "h":
                self.player.draw_card_from_deck()
                self.print_status()
            elif ans == "e" and first:
                print "The hint is: {0}".format(self.give_hint())
                # He can still use the first round options
                continue
            elif ans == "d" and first:
                self.bookie.double_bet()
                self.player.draw_card_from_deck()
                print "Betting on ${0}".format(self.bookie.bet)
                self.print_status()
                break
            elif ans == "r" and first:
                self.result.player_surrended()
                self.bookie.half_bet()
                break
            else:
                # In case no valid answer we want
                # The first status to be kept
                continue
            first = False

    def place_bet(self):
        bet = None
        while True:
            ans = raw_input(color("white") + "How much would you like to bet? \
(1, 5, 10, 50, 100, [s]ame): ")
            if ans is 's' or ans is '':
                if self.bookie.previous_bet is None:
                    print "No previous bet was made"
                    continue
                if self.bookie.credit < self.bookie.previous_bet:
                    print "You don't have enough credit for this bet"
                    continue
                bet = self.bookie.previous_bet
                break
            try:
                bet = int(ans)
            except:
                print "{0} is not a valid bet".format(ans)
                continue
            if [1, 5, 10, 50, 100].count(bet) is not 1:
                print "{0} is not a valid bet".format(ans)
                continue
            elif bet > self.bookie.credit:
                print "You only have {0} in credit".format(self.bookie.credit)
                continue
            break
        print "Betting on: ${0}".format(bet)
        self.bookie.place_bet(bet)

    def play(self):
        self.place_bet()
        self.start_game()
        if self.is_game_ended(no_more_moves=False):
            return
        self.player_turn()
        if self.is_game_ended(no_more_moves=False):
            return
        self.dealer_turn()
        if self.is_game_ended(no_more_moves=True):
            return


class GameSimulator(Game):

    bet = 100

    def player_turn(self):
        first = True
        ans = None
        while self.player.get_sum_of_cards() < 20 and ans != "s":
            if first:
                ans = self.give_hint()
                first = False
            else:
                if self.player.get_sum_of_cards() <= 12:
                    ans = "h"
                else:
                    ans = "s"
            if ans == "h":
                self.player.draw_card_from_deck()
                self.print_status()
            elif ans == "d":
                self.bookie.double_bet()
                self.player.draw_card_from_deck()
                print "Betting on ${0}".format(self.bookie.bet * 2)
                self.print_status()
            elif ans == "r":
                self.result.player_surrended()
                self.bookie.half_bet()
            else:
                ans = "s"

    def place_bet(self):
        print "Betting on: ${0}".format(self.bet)
        self.bookie.place_bet(self.bet)


def main():
    bookie = Bookie(credit=500)
    top_credit = bookie.credit
    games_played = 0
    print color("green") + "Your initial credit: {0}".format(bookie.credit)
    if "s" == raw_input("[S]imulator or [r]eal? "):
        while True:
            games_played += 1
            game = GameSimulator(bookie)
            game.play()
            if bookie.credit > top_credit:
                top_credit = bookie.credit
            print color("white") + "Your current credit: {0}".format(bookie.credit)
            if bookie.credit <= 0:
                print color("red") + "Man, you just lost everything..."
                break

    else:
        while True:
            games_played += 1
            game = Game(bookie)
            game.play()
            if bookie.credit > top_credit:
                top_credit = bookie.credit

            print color("white") + "Your current credit: {0}".format(bookie.credit)
            if bookie.credit > 0:
                if "n" == raw_input("Should we play another? (y/n): "):
                    break
            else:
                print color("red") + "Man, you just lost everything..."
                break
    print color("white") + "{0} games were played".format(games_played)
    print color("white") + "Your top credit was {0}".format(top_credit)
    print "End of game"


if __name__ == "__main__":
    main()
