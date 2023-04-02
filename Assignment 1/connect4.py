"""
FIT1045: Sem 1 2023 Assignment 1 (Solution Copy)
"""
import random
import os


def clear_screen():
    """
    Clears the terminal for Windows and Linux/MacOS.

    :return: None
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def print_rules():
    """
    Prints the rules of the game.

    :return: None
    """
    print("================= Rules =================")
    print("Connect 4 is a two-player game where the")
    print("objective is to get four of your pieces")
    print("in a row either horizontally, vertically")
    print("or diagonally. The game is played on a")
    print("6x7 grid. The first player to get four")
    print("pieces in a row wins the game. If the")
    print("grid is filled and no player has won,")
    print("the game is a draw.")
    print("=========================================")


def validate_input(prompt, valid_inputs):
    """
    Repeatedly ask user for input until they enter an input
    within a set valid of options.

    :param prompt: The prompt to display to the user, string.
    :param valid_inputs: The range of values to accept, list
    :return: The user's input, string.
    """
    # Implement your solution below
    while True:
        x = input(prompt)
        if x not in valid_inputs:
            print("Invalid input, please try again.")
        else:
            return x


def create_board():
    """
    Returns a 2D list of 6 rows and 7 columns to represent
    the game board. Default cell value is 0.

    :return: A 2D list of 6x7 dimensions.
    """
    # Implement your solution below
    return [[0 for _ in range(7)] for _ in range(6)]


def print_board(board):
    """
    Prints the game board to the console.

    :param board: The game board, 2D list of 6x7 dimensions.
    :return: None
    """
    # Implement your solution below
    print("========== Connect4 =========")
    print("Player 1: X       Player 2: O\n")
    print("  1   2   3   4   5   6   7")
    print(" --- --- --- --- --- --- ---")
    for i in range(len(board)):
        row = "|"
        for n in range(len(board[i])):
            if board[i][n] == 0:
                row += "   |"
            elif board[i][n] == 1:
                row += " X |"
            elif board[i][n] == 2:
                row += " O |"
        print(row)
        print(" --- --- --- --- --- --- ---")
    print("=============================")


def drop_piece(board, player, column):
    """
    Drops a piece into the game board in the given column.
    Please note that this function expects the column index
    to start at 1.

    :param board: The game board, 2D list of 6x7 dimensions.
    :param player: The player who is dropping the piece, int.
    :param column: The index of column to drop the piece into, int.
    :return: True if piece was successfully dropped, False if not.
    """
    # Implement your solution below
    column = int(column)
    i = len(board) - 1
    while i >= 0:
        if (board[i][column - 1] == 0):
            board[i][column - 1] = player
            return True
        i -= 1
    return False


def execute_player_turn(player, board):
    """
    Prompts user for a legal move given the current game board
    and executes the move.

    :return: Column that the piece was dropped into, int.
    """
    # Implement your solution below
    while True:
        column = validate_input(
            "Player " +
            str(player) + ", please enter the column you would like to drop your piece into: ",
            ["1", "2", "3", "4", "5", "6", "7"])
        if (drop_piece(board, player, column)):
            return int(column)
        else:
            print("That column is full, please try again.")


def end_of_game(board):
    """
    Checks if the game has ended with a winner
    or a draw.

    :param board: The game board, 2D list of 6 rows x 7 columns.
    :return: 0 if game is not over, 1 if player 1 wins, 2 if player 2 wins, 3 if draw.
    """
    # Implement your solution below
    def end_of_game(board):  # Question 6
        """
        Checks if the game has ended with a winner
        or a draw.

        :param board: The game board, 2D list of 6 rows x 7 columns.
        :return: 0 if game is not over, 1 if player 1 wins, 2 if player 2 wins, 3 if draw.
        """
        # Implement your solution below

        # replace 4 with the input number to win  :)

        empty = 0
        # Check for horizontal wins
        # not possible to win in the last 3 compile
        for c in range(len(board[0]) - 3):
            for r in range(len(board)):
                if board[r][c] != empty and all(board[r][c + i] == board[r][c] for i in range(4)):
                    return board[r][c]

        # Check for vertical wins
        for r in range(len(board) - 3):
            for c in range(len(board[0])):
                if board[r][c] != empty and all(board[r + i][c] == board[r][c] for i in range(4)):
                    return board[r][c]

        # Check for backwards \ diagonal wins
        for r in range(len(board) - 3):
            for c in range(3, len(board[0])):
                if board[r][c] != empty and all(board[r + i][c - i] == board[r][c] for i in range(4)):
                    return board[r][c]

        # Check for foward / diagonal wins
        for r in range(len(board) - 3):
            for c in range(len(board[0]) - 3):
                if board[r][c] != empty and all(board[r + i][c + i] == board[r][c] for i in range(4)):
                    return board[r][c]

        if 0 not in board[0]:
            return 3

        return 0


def local_2_player_game():
    """
    Runs a local 2 player game of Connect 4.

    :return: None
    """
    # Implement your solution below
    board = create_board()
    count = 0
    win = 0
    previous_turn = 0
    while win == 0:
        clear_screen()
        print_board(board)
        if (count >= 1):
            print("Player " + str((((count - 1) % 2) + 1)) +
                  " dropped a piece into column " + str(previous_turn))

        previous_turn = execute_player_turn((count % 2) + 1, board)

        if (count >= 6):
            win = end_of_game(board)
        count += 1
        print(win)

    print_board(board)
    print("Player " + str(win) + " has won!")
    input("Press return/enter to continue...")


def main():
    """
    Defines the main application loop.
User chooses a type of game to play or to exit.

    :return: None
    """
    # Implement your solution below
    user_input = ""
    while user_input != "4":
        print_main_menu()
        user_input = validate_input(
            "Select an option 1-4: ", ["1", "2", "3", "4"])
        if (user_input == "1"):
            print_rules()
            input("Press return/enter to continue...")
        elif (user_input == "2"):
            local_2_player_game()
        elif (user_input == "3"):
            game_against_cpu()  # does not work
        else:
            return

        clear_screen()


def print_main_menu():
    print("=============== Main Menu ===============")
    print("Welcome to Connect 4!")
    print("1. View Rules")
    print("2. Play a local 2 player game")
    print("3. Play a game against the computer")
    print("4. Exit")
    print("=========================================")


def cpu_player_easy(board, player):
    """
    Executes a move for the CPU on easy difficulty. This function 
    plays a randomly selected column.

    :param board: The game board, 2D list of 6x7 dimensions.
    :param player: The player whose turn it is, integer value of 1 or 2.
    :return: Column that the piece was dropped into, int.
    """
    # Implement your solution below
    while True:
        column = random.randint(1, 7)
        ran_drop = drop_piece(board, player, column)
        if ran_drop != 0:
            return column


def cpu_player_medium(board, player):
    """
    Executes a move for the CPU on medium difficulty. 
    It first checks for an immediate win and plays that move if possible. 
    If no immediate win is possible, it checks for an immediate win 
    for the opponent and blocks that move. If neither of these are 
    possible, it plays a random move.

    :param board: The game board, 2D list of 6x7 dimensions.
    :param player: The player whose turn it is, integer value of 1 or 2.
    :return: Column that the piece was dropped into, int.
    """
    # Implement your solution below
    temp_board = copy.deepcopy(board)
    enemy_player = 2 if player == 1 else 1

    for i in range(len(temp_board[0])):
        if drop_piece(temp_board, player, i):
            if (end_of_game(temp_board) != 0):
                drop_piece(board, player, i)
                return i

    temp_board = copy.deepcopy(board)

    for i in range(len(temp_board[0])):
        if drop_piece(temp_board, enemy_player, i):
            if (end_of_game(temp_board) != 0):
                drop_piece(board, player, i)
                return i

    indices = [i + 1 for i, element in enumerate(board[0]) if element == 0]
    rand_num = random.choice(indices)
    drop_piece(board, player, rand_num)
    # print_board(board)
    return rand_num


def cpu_player_hard(board, player):
    """
    Executes a move for the CPU on hard difficulty.
    This function creates a copy of the board to simulate moves.
    <Insert player strategy here>

    :param board: The game board, 2D list of 6x7 dimensions.
    :param player: The player whose turn it is, integer value of 1 or 2.
    :return: Column that the piece was dropped into, int.
    """
    # Implement your solution below
    raise NotImplementedError


def print_options():
    """
    Prints the options for playing against the computer

    :return: None
    """

    print("=============== Vs Computer =============")
    print("Select difficulty:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    print("4. Back")
    print("=========================================")


def game_against_cpu():
    """
    Runs a game of Connect 4 against the computer.

    :return: None
    """
    # Implement your solution below
    print_options()
    user_input = int(validate_input(
        "Select a number (1-4): ", ["1", "2", "3", "4"]))

    if user_input != 4:
        player = int(validate_input(
            "Would you like to be player 1 or 2? ", ["1", "2"]))
        cpu_player = 2 if player == 1 else 1
        board = create_board()
        count = 0
        win = 0
        previous_turn = 0
        while win == 0:
            clear_screen()
            print_board(board)
            if (count >= 1):
                print("Player " + str((((count - 1) % 2) + 1)) +
                      " dropped a piece into column " + str(previous_turn))

            if ((count % 2) + 1 == int(player)):
                previous_turn = execute_player_turn(player, board)
            else:
                if (user_input == 1):
                    previous_turn = cpu_player_easy(board, cpu_player)
                elif (user_input == 2):
                    previous_turn = cpu_player_medium(board, cpu_player)
                else:
                    previous_turn = cpu_player_hard(board, cpu_player)

            if (count >= 6):
                win = end_of_game(board)
            count += 1
            print(win)

        print_board(board)
        print("Player " + str(win) + " has won!")
        input("Press return/enter to continue...")


if __name__ == "__main__":
    main()
