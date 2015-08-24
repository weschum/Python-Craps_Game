#  Python 3.4.3
#  Author: Wes Chumley
#  Date:  July 2015

import random
import sys

from craps_text import Messages


class Craps:
    def setup(self):
        self.player_bank = 100
        self.point = None
        self.odds_bet = [] # [win, lose]

    def get_player(self):
        while True:
            begin = input('Would you like to begin?\n[Y]es or [N]o  > ')
            begin.lower()
            if begin in ['y', 'ye', 'yes', 'yeah', 'yep', 'yea']:
                player = 'yes'
                break
            elif begin in ['n', 'no', 'nop', 'nope']:
                player = 'no'
                break
            else:
                print("I don't understand your input.  Please try again.")
                continue
        return player

    def roll_dice(self):
        di_1, di_2 = random.randint(1, 6), random.randint(1, 6)
        return di_1 + di_2

    def set_point(self, roll):
        if roll in [2, 3, 7, 11, 12]:
            self.point = None
        if roll in [4, 5, 6, 8, 9, 10]:
            self.point = roll

    def show_bank(self):
        print('Player Bank: ${}'.format(self.player_bank))

    def calc_bank(self):
        # get player_bank
        # adjust player_bank according to result of turn
        # return adjusted player_bank
        pass

    def add_odds(self, point, answer):
        if answer in ['y', 'yes', 'yep', 'ye', 'yea', 'yeah']:
            if point == 4 or point == 10:
                odds_win, odds_lose = 10, 5  # $5 bet pays back $10
            if point == 5 or point == 9:
                odds_win, odds_lose = 7.5, 5  # $5 bet pays back $7.50
            if point == 6 or point == 8:
                odds_win, odds_lose = 6, 5  # $5 bet pays back $6
        else:
            odds_win, odds_lose = 0, 0
        self.odds_bet = [odds_win, odds_lose]

    def first_roll(self, roll):
        if roll in [7, 11]:
            self.player_bank += 5
            print("You win the turn and add $5 to your bank!")
            print("Player bank is now at ${}".format(self.player_bank))
        elif roll in [2, 3, 12]:
            self.player_bank -= 5
            print("CRAPS!!!  You lose the turn")
            print("Player bank is now ${}.".format(self.player_bank))
        else:
            self.point = roll
            print("Point is set at {}".format(roll))
            print(Messages.odds_msg)
            answer = input("Would you like to place an ODDS bet?\n[Y]es or [N]o  >  ")
            answer.lower()
            self.add_odds(roll, answer)

    def sub_roll(self, roll):
        if roll == self.point:
            self.player_bank += (5 + self.odds_bet[0])
            print("You hit the point to win the turn and add ${} to your bank!".format(
                5 + self.odds_bet[0]))
            print("Player bank is now at ${}".format(self.player_bank))
            self.point = None
        elif roll == 7:
            self.player_bank -= (5 + self.odds_bet[1])
            print("CRAP!  You hit seven and lose ${}.".format(5 + self.odds_bet[1]))
            print("Player bank is now at ${}".format(self.player_bank))
            self.point = None

    def play_game(self):
        while self.player_bank >= 5:
            action = input("Your move.  >  ")
            action.lower()
            if action in ['q', 'quit']:
                print("You have ${} in your bank.  Thanks for playing.".format(self.player_bank))
                sys.exit()
            if action in ['h', 'help']:
                print(Messages.game_help)
                continue
            if action == 'bank':
                self.show_bank()
                continue
            if action == 'point':
                print("The point is currently {}".format(self.point))
                continue
            if action in ['odd', 'odds']:
                print("The point odds is currently at {}".format(self.point_odds))
                continue
            #  Roll starts Here ________________________
            if action == 'roll':
                roll = self.roll_dice()
                print("You rolled {}".format(roll))
                if self.point == None:
                    self.first_roll(roll)
                    continue
                else:
                    self.sub_roll(roll)
                    continue

            else:
                print("Invalid input. Enter 'help' for game help")
                continue

        print('You have ${} in your bank. You need $5 or more to play.  Sorry.'.format(
            self.player_bank))
        sys.exit()

    def __init__(self):
        self.setup()
        print(Messages.welcome)
        choice = self.get_player()
        if choice == 'yes':
            print("Great. Let's get started.\n")
            print(Messages.game_help)
        if choice == 'no':
            print("Too bad.  Perhaps another time.\nGoodbye...  ")
            sys.exit()
        self.play_game()

        print(self.player_bank)
        print(self.point)
        print(self.come_out)
        print(self.point_odds)
        sys.exit()

Craps()
