

'''
Tic Tac Toe Draw
https://www.practicepython.org/exercise/2015/11/26/27-tic-tac-toe-draw.html

- For this exercise, assume that player 1 (the first player to move) will always be X and player 2 (the second player) will always be O.
- Notice how in the example I gave coordinates for where I want to move starting from (1, 1) instead of (0, 0). To people who don’t program, starting to count at 0 is a strange concept, so it is better for the user experience if the row counts and column counts start at 1. This is not required, but whichever way you choose to implement this, it should be explained to the player.
- Ask the user to enter coordinates in the form “row,col” - a number, then a comma, then a number. Then you can use your Python skills to figure out which row and column they want their piece to be in.
- Don’t worry about checking whether someone won the game, but if a player tries to put a piece in a game position where there already is another piece, do not allow the piece to go there.
'''

import logging



# get cordinate and return a tuple
def get_player_input(str_player):
    log = logging.getLogger("root")
    str_cordinates = input("%s, which col and row? " % str_player)
    log.debug("%s, input: %s" % (str_player, str_cordinates) )
    list_cord = str_cordinates.strip().split(',')
    return tuple(list_cord)


def tic_tac_toe_game():
    log = logging.getLogger("root")
    print("Welcome to tic tac toe")
    tup_p1 = get_player_input("Player 1")
    log.debug("Player 1: %s" % (tup_p1, ))
    
    
def main():
    logger = logging.getLogger("root")
    FORMAT = "[ %(filename)s:%(lineno)s - %(funcName)20s() ] %(message)s"
    logging.basicConfig(format=FORMAT)
    logger.setLevel(logging.DEBUG)
    tic_tac_toe_game()
    


if __name__ == '__main__':
    main()


