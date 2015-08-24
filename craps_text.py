# TEXT variables for Craps game

class Messages:
    welcome = '''
    Hello!
    Let's play a game of craps.\n
    Here's how the game works:\n
        At the beginning of each turn you will roll the dice.\n
        If your first roll is 7 or 11, you win the turn.
        If your first roll is 2, 3, or 12, you lose the turn.
        If your first roll is 4, 5, 6, 8, 9, or 10, you continue to roll until:
        \ta:    you roll your point (the value of your first roll) again, and win the turn, or
        \tb:    you roll a 7 and lose the turn.\n
        For each turn you will bet $5.  Your starting bank is $100.\n
        We will introduce ODDS later.
        '''
    game_help = '''
    ________________HELP____________________________________
    Any time you have a prompt (>), you can type the following commands:

    help -- gives you this help menu.
    quit -- prints the amount of your bank and quits the game
    bank -- prints the amount of your bank and continues game
    point -- prints the current 'point' value if one is established
    odds -- prints the odds payout for hitting the current 'point'
    roll -- continues your turn by executing the next roll
    _________________________________________________________
    '''

    odds_msg = '''
    Odds on 4 and 10 pay $10 on $5 bet
    Odds on 5 and 9 pay $7.50 on $5 bet
    Odds on 6 and 8 pay $6 on $5 bet
    '''
