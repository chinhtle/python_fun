from __future__ import print_function

BOARD_SIZE = 9
ROW_SEPARATOR = "-------------"
COLUMN_SEPARATOR = "|"
# Player 1 is "O" and player 2 is "X"
PLAYER_MARKER = ["O", "X"]
WINNING_POSITIONS = [[0, 1, 2], [3, 4, 5], [6, 7, 8], # Horizontals
                     [0, 3, 6], [1, 4, 7], [2, 5, 8], # Verticals
                     [0, 4, 8], [2, 4, 6]]            # Diagonals

board = None
gameover_status = None
current_player = None


def record_user_input(board, current_player):
    """
    Requests user input for the position they want to place a marker on
    and places marker on the position.
    """
    while True:
        try:
            position = int(raw_input("Please enter a position: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if 0 <= position < BOARD_SIZE:
            if mark_player_move(board, position, current_player):
                return
        else:
            print("Invalid range. Please try again.")


def print_board(board):
    """
    Prints markers placed on the board. If no marker is placed then
    the position number is printed.
    """
    position = 0
    print(ROW_SEPARATOR)
    for place in board:
        print(COLUMN_SEPARATOR, end="")
        val = place if place else position
        print(" {} ".format(str(val)), end="")

        position += 1
        if position % 3 == 0:
            print(COLUMN_SEPARATOR)
            print(ROW_SEPARATOR)


def check_game_status(board, current_player):
    """
    Checks the game status for the current player. Checks
    all winning positions for a win or a tie.
    Returns True if the game is over otherwise False.
    """
    if 0 not in board:
        print("No more moves left available! Tie game!")
        return True
    else:
        current_marker = PLAYER_MARKER[current_player]
        if board.count(current_marker) >= 3:
            for places in WINNING_POSITIONS:
                if (board[places[0]] == board[places[1]] ==
                        board[places[2]] == current_marker):
                    print("Player {} wins!".format(current_player + 1))
                    return True

    return False


def mark_player_move(board, position, current_player):
    """
    Takes the position as input for where the current user wants
    to place a marker. If a marker already exists at the position
    then return False, otherwise, a successful marking returns True.
    """
    # Check if the current spot has already been marked.
    if board[position] != 0:
        print("You can't make this move. Please try again.")
        return False

    board[position] = PLAYER_MARKER[current_player]
    return True


def switch_players(current_player):
    """
    Toggle between player one and player two.
    Returns the toggled value 0 or 1.
    """
    return not current_player


def replay_game():
    """
    Asks the user if the user wants to replay. Returns False if user enters 'y',
    otherwise returns False if user enters 'n'
    """
    replay = ""

    while not replay.startswith('y') and not replay.startswith('n'):
        replay = raw_input("Would you like to replay (y/n)? ").lower()

    return replay.startswith('y')


def reset_game():
    """
    Resets the game data and state.
    """
    global board, gameover_status, current_player

    board = [0] * BOARD_SIZE
    gameover_status = False
    current_player = 0


def main():
    """
    Starts a game of tic-tac-toe!
    """
    global board, gameover_status, current_player

    # Initialize the game
    reset_game()

    while not gameover_status:
        print_board(board)
        record_user_input(board, current_player)

        gameover_status = check_game_status(board, current_player)
        current_player = switch_players(current_player)

        if gameover_status:
            # Print ending board
            print_board(board)

            if replay_game():
                reset_game()
            else:
                break


if __name__ == "__main__":
    main()
