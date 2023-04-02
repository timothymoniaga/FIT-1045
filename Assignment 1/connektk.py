from math import ceil
import random
import copy
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


def validate_input_int(prompt):
    """
    Repeatedly ask user for input until they enter an input
    that is a digit.

    :param prompt: The prompt to display to the user, string.
    :return: The user's input, int.
    """
    # Implement your solution below
    while True:
        x = input(prompt)
        if not x.isdigit():
            print("Invalid input, please try again.")
        else:
            return int(x)


def create_board(columns, rows):
    """
    Returns a 2D list of 6 rows and 7 columns to represent
    the game board. Default cell value is 0.

    :columns: The number of columns in the array
    :rows: The number of rows in the array
    :return: A 2D list of columns x rows dimensions.
    """
    # Implement your solution below
    return [[0 for _ in range(columns)] for _ in range(rows)]


def print_board(board, num_players):
    """
    Prints the game board to the console.

    :param board: The game board, 2D list of 6x7 dimensions.
    :return: None
    """
    # Implement your solution below

    tokens = [" ", "X", "O", "!", "@", "#", "$", "%", "^", "&", "*", "+", "~"]
    seperator = ""
    numbers = ""
    legend = ""
    for _ in range(len(board[0])):
        seperator += " ---"
    
    for i in range(len(board)):
        numbers += "  " + str(i + 1) + " "

    for i in range(1, num_players + 1):
        legend += "P" + str(i) + ": " + tokens[i] + "  "


    print("========== Connectk =========")
    print(legend + "\n")
    print(numbers)
    print(seperator)
    for i in range(len(board)):
        row = "|"
        for n in range(len(board[i])):
            row += " " + tokens[board[i][n]] + " |"
        print(row)
        print(seperator)
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


def execute_player_turn(player, board, columns):
    """
    Prompts user for a legal move given the current game board
    and executes the move.

    :return: Column that the piece was dropped into, int.
    """
    # Implement your solution below
    valid_inputs = []
    for i in range(1, columns + 1):
        valid_inputs.append(str(i))

    while True:
        column = validate_input(
            "Player " +
            str(player) + ", please enter the column you would like to drop your piece into: ",
            valid_inputs)
        if (drop_piece(board, player, column)):
            return int(column)
        else:
            print("That column is full, please try again.")


def end_of_game(board, k):
    """
    Checks if the game has ended with a winner
    or a draw.

    :param board: The game board, 2D list of 6 rows x 7 columns.
    :return: 0 if game is not over, 1 if player 1 wins, 2 if player 2 wins, 3 if draw.
    """
    # Implement your solution below
    empty = 0
    # Check for horizontal wins
    # not possible to win in the last 3 compile
    for c in range(len(board[0]) - (k - 1)):
        for r in range(len(board)):
            if board[r][c] != empty and all(board[r][c + i] == board[r][c] for i in range(k)):
                return board[r][c]

    # Check for vertical wins
    for r in range(len(board) - (k - 1)):
        for c in range(len(board[0])):
            if board[r][c] != empty and all(board[r + i][c] == board[r][c] for i in range(k)):
                return board[r][c]

    # Check for backwards \ diagonal wins
    for r in range(len(board) - (k - 1)):
        for c in range((k - 1), len(board[0])):
            if board[r][c] != empty and all(board[r + i][c - i] == board[r][c] for i in range(k)):
                return board[r][c]

    # Check for foward / diagonal wins
    for r in range(len(board) - (k - 1)):
        for c in range(len(board[0]) - (k - 1)):
            if board[r][c] != empty and all(board[r + i][c + i] == board[r][c] for i in range(k)):
                return board[r][c]

    if 0 not in board[0]:
        return -1

    return 0


def main():
    """
    Defines the main application loop.
    User chooses a type of game to play or to exit.

    :return: None
    """
    rows = validate_input_int("Number of rows in game board: ")
    columns = validate_input_int("Number of columns in game board: ")
    board = create_board(columns, rows)
    k = validate_input_int(
        "Number of tokens to connect in order to win: ")
    num_human_players = validate_input_int("Number of human players: ")
    num_cpu_players = validate_input_int("Number of CPU players: ")
    players_order = []
    for i in range(1, num_human_players + 1):
        players_order.append(i)
    if num_cpu_players > 0:
        for i in range(num_cpu_players):
            difficulty = validate_input(
                "Select difficulty for cpu " + str(i + 1) + ": ", ["1", "2", "3"])
            players_order.append(difficulty)

    random.shuffle(players_order)
    play_connetk(board, players_order, k)


def play_connetk(board, player_order, k):
    """
    Playing the connectk code
    """
    win_flag = False
    player_type = ""
    previous_turn = 0
    winner = 0
    count = 0
    while win_flag == False:
        clear_screen()
        print_board(board, len(player_order))
        for i in range(len(player_order)):
            
            if player_type != "":
                print(player_type + str(((count - 1) % len(player_order)) + 1 ) + " dropped a piece into column " + str(previous_turn))
            
            if isinstance(player_order[i], str):
                difficulty = int(player_order[i])
                player_type = "CPU "
                if (difficulty == 1):
                    previous_turn = cpu_player_easy(board, i + 1)
                elif (difficulty == 2):
                    previous_turn = cpu_player_medium(board, i + 1, k)
                else:
                    previous_turn = cpu_player_hard(board, i + 1, k)
            else:
                previous_turn = execute_player_turn(i + 1, board, len(board[0]))
                player_type = "Player "
            
            count += 1
            print_board(board, len(player_order))
            winner = end_of_game(board, k)
            if winner != 0:
                win_flag = True
                break

    if(winner != -1):
        print(player_type + str(winner) + " has won!")
    else:
        print ("Draw!")


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


def cpu_player_medium(board, player, k):
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
            if (end_of_game(temp_board, k) != 0):
                drop_piece(board, player, i)
                return i

    temp_board = copy.deepcopy(board)

    for i in range(len(temp_board[0])):
        if drop_piece(temp_board, enemy_player, i):
            if (end_of_game(temp_board, k) != 0):
                drop_piece(board, player, i)
                return i

    indices = [i + 1 for i, element in enumerate(board[0]) if element == 0]
    rand_num = random.choice(indices)
    drop_piece(board, player, rand_num)
    # print_board(board)
    return rand_num


def cpu_player_hard(board, player, k):
    """
    Executes a move for the CPU on hard difficulty.
    This function creates a copy of the board to simulate moves.
    <Insert player strategy here>

    :param board: The game board, 2D list of 6x7 dimensions.
    :param player: The player whose turn it is, integer value of 1 or 2.
    :return: Column that the piece was dropped into, int.
    """
    # Implement your solution below
    temp_board = copy.deepcopy(board)
    enemy_player = 2 if player == 1 else 1

    for i in range(len(temp_board[0])):
        if drop_piece(temp_board, player, i):
            if (end_of_game(temp_board, k) != 0):
                drop_piece(board, player, i)
                return i

    temp_board = copy.deepcopy(board)

    for i in range(len(temp_board[0])):
        if drop_piece(temp_board, enemy_player, i):
            if (end_of_game(temp_board, k) != 0):
                drop_piece(board, player, i)
                return i

    indices = [i + 1 for i, element in enumerate(board[0]) if element == 0]
    sorted_indicies = sorted(
        indices, key=lambda x: get_distance_from_target(x, target=(ceil(len(board[0])/2))))
    best_columns = sorted_indicies[:(len(board[0])//2)]
    rand_num = random.choice(best_columns)
    drop_piece(board, player, rand_num)
    return rand_num


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
    print("=========================================")

def get_distance_from_target(num, target):
    return abs(target - num)



if __name__ == "__main__":
    main()
